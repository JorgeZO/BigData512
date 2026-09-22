"""Ejecuta todas las celdas con el Python actual y guarda sus salidas."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager


def main():
    raiz = Path(__file__).resolve().parents[1]
    ruta = raiz / 'notebook' / 'U3_1_modelos_regresion_demografia.ipynb'
    notebook = nbformat.read(ruta, as_version=4)
    km = KernelManager(kernel_name='python3')
    km.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
    cliente = NotebookClient(notebook, km=km, timeout=180,
                             resources={'metadata': {'path': str(ruta.parent)}})
    cliente.execute(cleanup_kc=True)
    nbformat.validate(notebook)
    nbformat.write(notebook, ruta)
    print(f'Notebook ejecutado sin errores: {ruta.name}')


if __name__ == '__main__':
    main()
