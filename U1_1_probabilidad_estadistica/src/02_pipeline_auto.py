from pathlib import Path
import sys
import pandas as pd
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent / "scripts"))
from curso import leer_owid, metadatos

df = leer_owid("life-expectancy")
metadata = metadatos("life-expectancy")

# ============================================================
# 3. FUNCIÓN DEL PIPELINE
# ============================================================

def ejecutar_pipeline(df):

    print("============================================")
    print("INICIO DEL PIPELINE")
    print("============================================")

    # --------------------------------------------------------
    # 3.1 Dimensiones iniciales
    # --------------------------------------------------------

    print("\nDimensiones iniciales:")
    print(df.shape)

    # --------------------------------------------------------
    # 3.2 Identificar las columnas disponibles
    # --------------------------------------------------------

    print("\nColumnas disponibles:")
    print(df.columns.tolist())

    # --------------------------------------------------------
    # 3.3 Tipos de datos
    # --------------------------------------------------------

    print("\nTipos de datos:")
    print(df.dtypes)

    # --------------------------------------------------------
    # 3.4 Valores nulos
    # --------------------------------------------------------

    print("\nValores nulos:")
    print(df.isnull().sum())

    # --------------------------------------------------------
    # 3.5 Eliminar filas con valores nulos
    # --------------------------------------------------------

    df = df.dropna()

    print("\nDimensiones después de eliminar nulos:")
    print(df.shape)

    # --------------------------------------------------------
    # 3.6 Eliminar posibles filas duplicadas
    # --------------------------------------------------------

    df = df.drop_duplicates()

    print("\nDimensiones después de eliminar duplicados:")
    print(df.shape)

    # --------------------------------------------------------
    # 3.7 Resultado
    # --------------------------------------------------------

    archivo_salida = ROOT / "data" / "processed" / "auto_resultado.csv"
    archivo_salida.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(
        archivo_salida,
        index=False
    )

    print("\n============================================")
    print("PIPELINE FINALIZADO")
    print("============================================")

    print(f"\nArchivo generado:")
    print(archivo_salida)

    return df


# ============================================================
# 4. EJECUCIÓN DEL PIPELINE
# ============================================================

df_procesado = ejecutar_pipeline(df)