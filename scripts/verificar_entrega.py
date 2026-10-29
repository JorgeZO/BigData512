"""Comprueba ejecución completa, fuentes, llaves y exportaciones de la entrega."""
from hashlib import sha256
from pathlib import Path
import ast
import json
import nbformat
import pandas as pd
from ejecutar_practicas import PRACTICAS

RAIZ = Path(__file__).resolve().parents[1]


def main():
    errores = []
    celdas_ejecutadas = 0
    for archivo in PRACTICAS:
        ruta = RAIZ / archivo
        notebook = nbformat.read(ruta, as_version=4)
        nbformat.validate(notebook)
        for i, celda in enumerate(notebook.cells):
            if celda.cell_type != "code" or not celda.source.strip(): continue
            ast.parse(celda.source, filename=f"{archivo}:celda{i}")
            if celda.execution_count is None: errores.append(f"Celda no ejecutada: {archivo}:{i}")
            celdas_ejecutadas += 1
            for salida in celda.outputs:
                if salida.output_type == "error": errores.append(f"Error guardado: {archivo}:{i}")
                if salida.output_type == "stream" and any(s in salida.text for s in ["ConvergenceWarning", "Traceback"]):
                    errores.append(f"Advertencia pendiente: {archivo}:{i}")
        for extension in ["html", "pdf"]:
            salida = RAIZ / f"reportes/{extension}/{ruta.stem}.{extension}"
            if not salida.is_file() or salida.stat().st_size == 0: errores.append(f"Falta reporte: {salida}")
    for manifest, prefijo in [("manifest.json", RAIZ/"datos_fuente"), ("material_clase.json", RAIZ)]:
        for registro in json.loads((RAIZ/"datos_fuente"/manifest).read_text()):
            archivo = prefijo/registro["archivo"]
            if sha256(archivo.read_bytes()).hexdigest() != registro["sha256"]:
                errores.append(f"Fuente alterada: {archivo}")
    integrado = pd.read_csv(RAIZ/"U3_1_modelos_ml/data/dataset_health_gdp_demografia_final.csv")
    esperado = ["entity", "year", "population", "births", "deaths", "child_deaths_under_5", "percentage_health", "gdp"]
    if integrado.columns.tolist() != esperado: errores.append("La tarea no tiene las ocho columnas solicitadas")
    for nombre in ["demografia_owid_2000_2022.csv", "demografia_china_mexico_completo.csv"]:
        tabla = pd.read_csv(RAIZ/"U3_1_modelos_ml/data/processed"/nombre)
        if tabla.duplicated(["entity", "year"]).any(): errores.append(f"Llaves duplicadas: {nombre}")
    for archivo in RAIZ.rglob("*.py"):
        if ".venv" not in archivo.parts: ast.parse(archivo.read_text(), filename=str(archivo))
    if errores: raise SystemExit("\n".join(errores))
    print(f"Entrega verificada: {len(PRACTICAS)} notebooks, {celdas_ejecutadas} celdas ejecutadas, fuentes íntegras y 28 reportes HTML/PDF.")


if __name__ == "__main__": main()
