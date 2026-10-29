"""Ejecuta y exporta la práctica de regresión desde el ejecutor común."""
from pathlib import Path
import subprocess
import sys

if __name__ == "__main__":
    raiz = Path(__file__).resolve().parents[2]
    subprocess.run([sys.executable, str(raiz / "scripts/ejecutar_practicas.py"),
                    "--desde", "4", "--hasta", "4"], check=True, cwd=raiz)
