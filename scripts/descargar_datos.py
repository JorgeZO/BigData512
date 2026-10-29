"""Descarga fuentes públicas y registra sus huellas; no descarga soluciones."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import requests

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "datos_fuente"
SLUGS = [
    "children-born-per-woman", "life-expectancy",
    "life-expectancy-at-birth-including-the-un-projections",
    "population-with-un-projections", "number-of-births-per-year",
    "number-of-deaths-per-year", "number-of-child-deaths-unwpp",
    "total-healthcare-expenditure-gdp", "gdp-per-capita-worldbank", "migrant-populations",
]
SUFIJO = "?v=1&csvType=full&useColumnShortNames=true"


def descargar(tarea):
    archivo, url, fuente = tarea
    ruta = DESTINO / archivo
    respuesta = requests.get(url, timeout=120,
                             headers={"User-Agent": "BigData512 educational analysis"})
    respuesta.raise_for_status()
    if archivo.endswith(".csv") and respuesta.content.lstrip().startswith(b"<"):
        raise ValueError(f"Se recibió HTML en lugar de CSV: {url}")
    if archivo.endswith(".json"):
        respuesta.json()
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(respuesta.content)
    print(f"Descargado: {archivo} ({len(respuesta.content):,} bytes)", flush=True)
    return {"archivo": archivo, "url": url, "fuente": fuente,
            "sha256": sha256(respuesta.content).hexdigest(),
            "bytes": len(respuesta.content),
            "descargado_utc": datetime.now(timezone.utc).isoformat()}


def main():
    tareas = []
    for slug in SLUGS:
        for extension in ("csv", "metadata.json"):
            parametros = SUFIJO + ("&metric=immigrants&unit=number" if slug == "migrant-populations" else "")
            tareas.append((f"owid/{slug}.{extension}",
                           f"https://ourworldindata.org/grapher/{slug}.{extension}{parametros}",
                           "Our World in Data; consultar metadatos por indicador"))
    tareas.append(("uci/wholesale_customers.csv",
                   "https://archive.ics.uci.edu/static/public/292/wholesale+customers.zip",
                   "Cardoso, M. (2013). UCI. DOI: 10.24432/C5030X"))
    # El ZIP de UCI se conserva como fuente y se extrae sin alterar sus filas.
    tareas[-1] = ("uci/wholesale_customers.zip", tareas[-1][1], tareas[-1][2])
    with ThreadPoolExecutor(max_workers=4) as pool:
        registros = list(pool.map(descargar, tareas))
    import zipfile
    with zipfile.ZipFile(DESTINO / "uci/wholesale_customers.zip") as paquete:
        nombre = next(n for n in paquete.namelist() if n.lower().endswith(".csv"))
        contenido = paquete.read(nombre)
    (DESTINO / "uci/wholesale_customers.csv").write_bytes(contenido)
    registros.append({"archivo": "uci/wholesale_customers.csv",
                      "extraido_de": "uci/wholesale_customers.zip",
                      "sha256": sha256(contenido).hexdigest(), "bytes": len(contenido)})
    (DESTINO / "manifest.json").write_text(
        json.dumps(registros, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
