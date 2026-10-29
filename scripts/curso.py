"""Rutas y lectura de fuentes; los análisis se desarrollan en cada notebook."""
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parents[1]
FUENTES = RAIZ / "datos_fuente"
U1 = RAIZ / "U1_1_probabilidad_estadistica"
U3 = RAIZ / "U3_1_modelos_ml"
SALIDA = U3 / "data" / "processed"
FIGURAS = RAIZ / "reportes" / "figuras"
for carpeta in (SALIDA, FIGURAS, U1 / "data/processed"):
    carpeta.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({"figure.figsize": (9, 4), "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True,
                     "grid.alpha": .22, "figure.dpi": 110,
                     "axes.prop_cycle": plt.cycler(color=["#146c94", "#dc7827", "#3c896d", "#8661a6"]),
                     "savefig.bbox": "tight"})


def leer_owid(slug):
    ruta = FUENTES / "owid" / f"{slug}.csv"
    if not ruta.exists():
        raise FileNotFoundError(f"Falta {ruta.name}; ejecutar scripts/descargar_datos.py")
    return pd.read_csv(ruta)


def metadatos(slug):
    return json.loads((FUENTES / "owid" / f"{slug}.metadata.json").read_text(encoding="utf-8"))


def indicador(slug, columna, nombre):
    tabla = leer_owid(slug)
    if columna not in tabla:
        raise KeyError(f"Cambió el esquema de {slug}; columnas disponibles: {tabla.columns.tolist()}")
    tabla = tabla[["entity", "code", "year", columna]].rename(columns={columna: nombre})
    if tabla.duplicated(["entity", "year"]).any():
        raise ValueError(f"Llaves duplicadas en {slug}")
    return tabla


def solo_paises(tabla):
    """Universo explícito: códigos de tres letras; excluye agregados OWID."""
    return tabla.loc[tabla["code"].astype("string").str.fullmatch(r"[A-Z]{3}", na=False)].copy()


def guardar_figura(nombre):
    plt.tight_layout()
    plt.savefig(FIGURAS / f"{nombre}.png", dpi=150)
    plt.show()
    plt.close()


def guardar_tabla(tabla, nombre, carpeta=SALIDA):
    carpeta.mkdir(parents=True, exist_ok=True)
    tabla.to_csv(carpeta / nombre, index=False)
    print(f"CSV guardado: {(carpeta / nombre).relative_to(RAIZ)} ({len(tabla):,} filas)")
