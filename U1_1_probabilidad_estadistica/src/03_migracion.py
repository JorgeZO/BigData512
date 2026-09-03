from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent.parent

# ============================================================
# 1. EXTRACCIÓN — Fetch the data
# ============================================================

url_datos = (
    "https://ourworldindata.org/grapher/migrant-populations.csv"
    "?v=1&csvType=full&useColumnShortNames=true"
    "&metric=immigrants&unit=number"
)

df = pd.read_csv(
    url_datos,
    storage_options={
        "User-Agent": "Our World In Data data fetch/1.0"
    }
)

# ============================================================
# 2. EXTRACCIÓN — Fetch the metadata
# ============================================================

url_metadata = (
    "https://ourworldindata.org/grapher/migrant-populations.metadata.json"
    "?v=1&csvType=full&useColumnShortNames=true"
    "&metric=immigrants&unit=number"
)

metadata = requests.get(url_metadata).json()

# ============================================================
# 3. EXPLORACIÓN INICIAL
# ============================================================

print("Dimensiones del DataFrame:")
print(df.shape)

print("\nColumnas:")
print(df.columns.tolist())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isnull().sum())

# ============================================================
# 4. LIMPIEZA
# ============================================================

# Eliminar registros que no tengan código de país
df = df.dropna(subset=["code"])

# Eliminar registros que no tengan número de inmigrantes
df = df.dropna(subset=["immigrants_all"])

# ============================================================
# 5. TRANSFORMACIÓN
# ============================================================

df["Year"] = df["year"].astype(int)
df["immigrants_all"] = df["immigrants_all"].astype(int)

# ============================================================
# 6. FILTRADO
# ============================================================

# Trabajaremos únicamente con datos a partir del año 2000
df = df[df["year"] >= 2000]

# ============================================================
# 7. ANÁLISIS
# ============================================================

# Promedio de inmigrantes por país
promedio_pais = (
    df.groupby("entity")["immigrants_all"]
      .mean()
      .round(0)
      .astype(int)
      .sort_values(ascending=False)
)

print("\nPromedio de inmigrantes por país:")
print(promedio_pais.head(10))

# ============================================================
# 8. RESULTADO
# ============================================================

archivo_salida = ROOT / "data" / "processed" / "promedio_inmigrantes_por_pais.csv"
archivo_salida.parent.mkdir(parents=True, exist_ok=True)

promedio_pais.to_csv(
    archivo_salida,
    header=["Average immigrants"]
)

print("\nPipeline ejecutado correctamente.")
print(f"Archivo generado: {archivo_salida}")
