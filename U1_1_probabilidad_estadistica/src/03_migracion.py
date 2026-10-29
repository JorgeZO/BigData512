from pathlib import Path
import sys
import pandas as pd
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent / "scripts"))
from curso import leer_owid, metadatos

df = leer_owid("migrant-populations")
metadata = metadatos("migrant-populations")

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
df = df.dropna(subset=["immigrants_all"]).copy()

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
