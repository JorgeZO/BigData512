# Práctica 1.1 — Probabilidad y Estadística

Análisis de la evolución poblacional mundial con datos de Our World in Data (fuente original: United Nations, World Population Prospects 2024).

## Objetivo

Comprobar el entorno de análisis de datos y aplicar medidas estadísticas descriptivas básicas con Pandas y NumPy.

## Estructura

```text
U1_1_probabilidad_estadistica/
├── .venv/
├── data/
│   ├── raw/
│   │   ├── annual_population_growth/
│   │   └── births_deaths/
│   └── processed/
├── notebooks/
│   ├── 01_evolucion_poblacional.ipynb
│   └── 02_transformaciones.ipynb
├── src/
│   ├── 01_pipeline.py
│   ├── 02_pipeline_auto.py
│   └── 03_migracion.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Datos

El análisis de la práctica se realiza con `data/raw/annual_population_growth/annual-population-growth.csv`. La carpeta `births_deaths` se conserva como parte de los datos proporcionados, sin modificar los archivos originales.

Los archivos `.metadata.json` y `readme.md` se mantienen porque documentan la fuente, las variables y el procesamiento.

## Notebooks

- `01_evolucion_poblacional.ipynb`: actividades 1 a 4 de la práctica (fuente, exploración, estadística descriptiva y comprobación del entorno), más ejercicios de clase (`loc`/`iloc` y filtro por apellido).
- `02_transformaciones.ipynb`: carga de datos desde la API de Our World in Data y transformaciones básicas.

## Scripts

- `01_pipeline.py`: pipeline de esperanza de vida.
- `02_pipeline_auto.py`: pipeline automático de limpieza.
- `03_migracion.py`: pipeline equivalente usando el dataset de poblaciones migrantes (inmigrantes), en lugar de fertilidad.

## Entorno

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

La carpeta `.venv` no se incluye en el repositorio.
