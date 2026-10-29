"""Ejecuta las prácticas en orden, rechaza errores y exporta HTML actualizado."""
from datetime import datetime, timezone
from pathlib import Path
from time import monotonic
import argparse
import json
import platform
import sys
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from jupyter_client import KernelManager

RAIZ = Path(__file__).resolve().parents[1]
PRACTICAS = [
    "U1_1_probabilidad_estadistica/notebooks/01_evolucion_poblacional.ipynb",
    "U1_1_probabilidad_estadistica/notebooks/02_transformaciones.ipynb",
    "U1_1_probabilidad_estadistica/notebooks/03_fertility_rate.ipynb",
    "U3_1_modelos_ml/notebook/U3_1_modelos_regresion_demografia.ipynb",
    "U3_1_modelos_ml/notebooks/04_healthcare_spending.ipynb",
    "U3_1_modelos_ml/notebooks/05_gdp_per_capita.ipynb",
    "U3_1_modelos_ml/notebooks/06_relacion_salud_vs_gdp.ipynb",
    "U3_1_modelos_ml/notebooks/U3_2_Preparacion_dataset.ipynb",
    "U3_1_modelos_ml/notebooks/tarea_dataset_health_gdp.ipynb",
    "U3_1_modelos_ml/notebooks/U3_2_China-Mexico.ipynb",
    "U3_1_modelos_ml/notebooks/U3_4_proyecciones_2100.ipynb",
    "U3_1_modelos_ml/notebooks/U4_1_Clustering_Wholesale_Customers.ipynb",
    "U3_1_modelos_ml/notebooks/U4_2_Clustering_Online_Retail_Customers.ipynb",
    "U3_1_modelos_ml/notebooks/U4_3_Plantilla_Clustering_Online_retail.ipynb",
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--desde", type=int, default=1, help="Número inicial de práctica (1 a 14)")
    parser.add_argument("--hasta", type=int, default=len(PRACTICAS), help="Número final inclusive")
    args = parser.parse_args()
    registros = []
    destino = RAIZ / "reportes/html"
    destino.mkdir(parents=True, exist_ok=True)
    for indice, archivo in enumerate(PRACTICAS, 1):
        if not args.desde <= indice <= args.hasta:
            continue
        ruta = RAIZ / archivo
        inicio = monotonic()
        notebook = nbformat.read(ruta, as_version=4)
        for celda in notebook.cells:
            if celda.cell_type == "code":
                celda.outputs = []
                celda.execution_count = None
        km = KernelManager(kernel_name="python3")
        km.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
        cliente = NotebookClient(notebook, km=km, timeout=240, allow_errors=False,
                                 resources={"metadata": {"path": str(ruta.parent)}})
        print(f"[{indice}/{len(PRACTICAS)}] Ejecutando {ruta.name}", flush=True)
        cliente.execute(cleanup_kc=True)
        nbformat.validate(notebook)
        nbformat.write(notebook, ruta)
        html, _ = HTMLExporter(template_name="lab").from_notebook_node(notebook)
        (destino / f"{ruta.stem}.html").write_text(html, encoding="utf-8")
        duracion = round(monotonic() - inicio, 2)
        registros.append({"notebook": archivo, "resultado": "correcto", "segundos": duracion,
                          "celdas_codigo": sum(c.cell_type == "code" for c in notebook.cells)})
        print(f"  Correcto ({duracion:.1f} s)", flush=True)
    import pandas, numpy, sklearn, matplotlib
    informe = {"ejecutado_utc": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
               "versiones": {"pandas": pandas.__version__, "numpy": numpy.__version__,
                             "scikit-learn": sklearn.__version__, "matplotlib": matplotlib.__version__},
               "practicas": registros}
    nombre = "validacion.json" if args.desde == 1 and args.hasta == len(PRACTICAS) else f"validacion_{args.desde}_{args.hasta}.json"
    (RAIZ / "reportes" / nombre).write_text(json.dumps(informe, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
