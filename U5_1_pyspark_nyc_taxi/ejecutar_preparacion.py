"""Ejecuta U5.1 con el Python actual y registra una comprobación local real."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from time import monotonic
import json
import os
import platform
import re
import subprocess
import sys

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from jupyter_client import KernelManager

RAIZ = Path(__file__).resolve().parent
NOMBRE = "U5_1_preparation_pyspark_NYC_taxi.ipynb"


def configurar():
    archivo = RAIZ / ".runtime-local.json"
    configuracion = json.loads(archivo.read_text()) if archivo.exists() else {}
    java_home = configuracion.get("JAVA_HOME") or os.environ.get("JAVA_HOME")
    if not java_home and sys.platform == "darwin":
        r = subprocess.run(["/usr/libexec/java_home", "-v", "17"], capture_output=True, text=True)
        if r.returncode == 0: java_home = r.stdout.strip()
    if not java_home or not (Path(java_home)/"bin/java").exists():
        raise SystemExit("Configura JAVA_HOME con un JDK 17 compatible antes de ejecutar.")
    temporal = RAIZ / ".spark-tmp"
    temporal.mkdir(exist_ok=True)
    os.environ.update({"JAVA_HOME": java_home, "PATH": str(Path(java_home)/"bin")+os.pathsep+os.environ["PATH"],
        "PYSPARK_PYTHON": sys.executable, "PYSPARK_DRIVER_PYTHON": sys.executable,
        "SPARK_LOCAL_IP": "127.0.0.1", "SPARK_LOCAL_DIRS": str(temporal),
        "IPYTHONDIR": str(temporal/"ipython"), "JUPYTER_RUNTIME_DIR": str(temporal/"jupyter")})
    return subprocess.run([str(Path(java_home)/"bin/java"), "-version"],
                          capture_output=True, text=True, check=True).stderr.splitlines()[0]


def main():
    java = configurar()
    ruta = RAIZ / "notebooks" / NOMBRE
    notebook = nbformat.read(ruta, as_version=4)
    for celda in notebook.cells:
        if celda.cell_type == "code":
            celda.outputs = []
            celda.execution_count = None
    notebook.metadata.kernelspec = {"display_name": "U5 NYC Taxi (.venv Python 3.12)",
                                   "language": "python", "name": "python3"}
    manager = KernelManager(kernel_name="python3")
    manager.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
    cliente = NotebookClient(notebook, km=manager, timeout=300, allow_errors=False,
                             resources={"metadata": {"path": str(ruta.parent)}})
    inicio = monotonic()
    print("Ejecutando todas las celdas de U5.1...", flush=True)
    cliente.execute(cleanup_kc=True)
    nbformat.validate(notebook)
    nbformat.write(notebook, ruta)
    errores = [o for c in notebook.cells for o in c.get("outputs", []) if o.output_type == "error"]
    assert not errores
    texto = "\n".join(str(o.get("text", "")) for c in notebook.cells for o in c.get("outputs", []))
    coincidencia = re.search(r"Registros de la muestra:\s*(\d+)", texto)
    assert coincidencia and int(coincidencia.group(1)) == 1000, "La muestra no contiene las 1000 filas esperadas."
    filas = re.search(r"Filas totales declaradas:\s*(\d+)", texto)
    grupos = re.search(r"Grupos de filas:\s*(\d+)", texto)
    procedencia = json.loads((RAIZ / "origen_notebook.json").read_text())
    originales = [c for c in notebook.cells if "codigo-original-u5-1" in c.metadata.get("tags", [])]
    assert len(originales) == 6
    assert [sha256(c.source.encode()).hexdigest() for c in originales] == procedencia["sha256_celdas_codigo_originales"]
    import pyspark, pyarrow
    salida = RAIZ / "evidencia"
    salida.mkdir(exist_ok=True)
    html, _ = HTMLExporter(template_name="lab").from_notebook_node(notebook)
    (salida / NOMBRE.replace(".ipynb", ".html")).write_text(html, encoding="utf-8")
    informe = {"ejecutado_utc": datetime.now(timezone.utc).isoformat(), "resultado": "correcto",
        "python": platform.python_version(), "pyspark": pyspark.__version__, "pyarrow": pyarrow.__version__,
        "java": java, "sistema": platform.system(), "arquitectura": platform.machine(),
        "master": "local[*]", "celdas_codigo": sum(c.cell_type=="code" for c in notebook.cells),
        "celdas_originales_conservadas": 6, "filas_muestra": 1000,
        "filas_parquet_declaradas": int(filas.group(1)), "grupos_filas_parquet": int(grupos.group(1)),
        "archivos_parquet_guardados_en_la_practica": [str(p.relative_to(RAIZ)) for p in RAIZ.rglob("*.parquet") if ".venv" not in p.parts],
        "errores": len(errores), "segundos": round(monotonic()-inicio, 2),
        "sha256_notebook_ejecutado": sha256(ruta.read_bytes()).hexdigest(),
        "alcance": "Muestra local de 1000 filas y tres columnas; Parquet consultado por rangos HTTP, sin guardar el dataset completo."}
    (salida / "ejecucion_local.json").write_text(json.dumps(informe, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(informe, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__": main()
