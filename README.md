# Tópicos de Big Data · Grupo 512

**Jorge Adalberto Zuñiga Oliva · Matrícula 82005 · JorgeZO**

Prácticas con desarrollo, respuestas, tablas, gráficas y salidas de ejecución. El índice cubre
las actividades identificadas en el material de referencia del curso, excepto los exámenes.
Los reportes PDF resumen los análisis; los notebooks contienen el desarrollo completo y los HTML
permiten consultarlo sin ejecutar Python.

## Prácticas

| # | Práctica | Notebook con código y resultados | Reporte |
|---:|---|---|---|
| 1 | Evolución poblacional y estadística | [Abrir](U1_1_probabilidad_estadistica/notebooks/01_evolucion_poblacional.ipynb) | [HTML](reportes/html/01_evolucion_poblacional.html) · [PDF](reportes/pdf/01_evolucion_poblacional.pdf) |
| 2 | Transformaciones de esperanza de vida | [Abrir](U1_1_probabilidad_estadistica/notebooks/02_transformaciones.ipynb) | [HTML](reportes/html/02_transformaciones.html) · [PDF](reportes/pdf/02_transformaciones.pdf) |
| 3 | Fecundidad México-Japón | [Abrir](U1_1_probabilidad_estadistica/notebooks/03_fertility_rate.ipynb) | [HTML](reportes/html/03_fertility_rate.html) · [PDF](reportes/pdf/03_fertility_rate.pdf) |
| 4 | Regresión demográfica de México | [Abrir](U3_1_modelos_ml/notebook/U3_1_modelos_regresion_demografia.ipynb) | [HTML](reportes/html/U3_1_modelos_regresion_demografia.html) · [PDF](reportes/pdf/U3_1_modelos_regresion_demografia.pdf) |
| 5 | Gasto en salud | [Abrir](U3_1_modelos_ml/notebooks/04_healthcare_spending.ipynb) | [HTML](reportes/html/04_healthcare_spending.html) · [PDF](reportes/pdf/04_healthcare_spending.pdf) |
| 6 | PIB per cápita | [Abrir](U3_1_modelos_ml/notebooks/05_gdp_per_capita.ipynb) | [HTML](reportes/html/05_gdp_per_capita.html) · [PDF](reportes/pdf/05_gdp_per_capita.pdf) |
| 7 | Relación salud-ingreso | [Abrir](U3_1_modelos_ml/notebooks/06_relacion_salud_vs_gdp.ipynb) | [HTML](reportes/html/06_relacion_salud_vs_gdp.html) · [PDF](reportes/pdf/06_relacion_salud_vs_gdp.pdf) |
| 8 | Preparación del panel demográfico | [Abrir](U3_1_modelos_ml/notebooks/U3_2_Preparacion_dataset.ipynb) | [HTML](reportes/html/U3_2_Preparacion_dataset.html) · [PDF](reportes/pdf/U3_2_Preparacion_dataset.pdf) |
| 9 | Dataset integrado de salud e ingreso | [Abrir](U3_1_modelos_ml/notebooks/tarea_dataset_health_gdp.ipynb) | [HTML](reportes/html/tarea_dataset_health_gdp.html) · [PDF](reportes/pdf/tarea_dataset_health_gdp.pdf) |
| 10 | Regresión México-China | [Abrir](U3_1_modelos_ml/notebooks/U3_2_China-Mexico.ipynb) | [HTML](reportes/html/U3_2_China-Mexico.html) · [PDF](reportes/pdf/U3_2_China-Mexico.pdf) |
| 11 | Series de tiempo, red neuronal y escenarios | [Abrir](U3_1_modelos_ml/notebooks/U3_4_proyecciones_2100.ipynb) | [HTML](reportes/html/U3_4_proyecciones_2100.html) · [PDF](reportes/pdf/U3_4_proyecciones_2100.pdf) |
| 12 | Clientes mayoristas | [Abrir](U3_1_modelos_ml/notebooks/U4_1_Clustering_Wholesale_Customers.ipynb) | [HTML](reportes/html/U4_1_Clustering_Wholesale_Customers.html) · [PDF](reportes/pdf/U4_1_Clustering_Wholesale_Customers.pdf) |
| 13 | Clientes de Online Retail | [Abrir](U3_1_modelos_ml/notebooks/U4_2_Clustering_Online_Retail_Customers.ipynb) | [HTML](reportes/html/U4_2_Clustering_Online_Retail_Customers.html) · [PDF](reportes/pdf/U4_2_Clustering_Online_Retail_Customers.pdf) |
| 14 | Líneas de venta de Online Retail | [Abrir](U3_1_modelos_ml/notebooks/U4_3_Plantilla_Clustering_Online_retail.ipynb) | [HTML](reportes/html/U4_3_Plantilla_Clustering_Online_retail.html) · [PDF](reportes/pdf/U4_3_Plantilla_Clustering_Online_retail.pdf) |

Las 14 prácticas fueron ejecutadas en el orden del índice. El registro de versiones, ejecución y
huellas de los notebooks está en [reportes/validacion.json](reportes/validacion.json).
El [mapa de cobertura](COBERTURA.md) relaciona el temario de referencia con cada entrega.

## Investigaciones

- [Preparación, modelos y evaluación de ML](investigaciones/01_machine_learning.md) · [PDF](<Actividad de investigación Machine Learning.pdf>)
- [Metodología de proyecciones demográficas](investigaciones/02_modelo_predictivo.md) · [PDF](<Investigación Modelo predictivo.pdf>)
- [KNN y ejemplo reproducible](investigaciones/03_knn.md) · [PDF](<KNN (K-Nearest Neighbors) Investigación.pdf>)
- [Resumen cuantitativo de regresión](investigaciones/04_resumen_regresion.md) · [PDF](<Resumen_Modelos_Regresion.pdf>)
- [Análisis de lectura sobre esperanza de vida](investigaciones/05_lectura_esperanza_vida.md) · [PDF](<Why is life expectancy in the US lower than in other rich countries.pdf>)

El ejemplo de KNN se puede ejecutar por separado: `python investigaciones/ejemplo_knn.py`.
Su [resultado guardado](reportes/knn_resultados.json) incluye selección de k, métricas y matriz de confusión.

## Ejecutar el trabajo

Se recomienda Python 3.11 o posterior; los notebooks se comprobaron con Python 3.13 y las versiones
de [requirements.txt](requirements.txt). Desde la carpeta raíz:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

En Windows, la activación equivalente es `.venv\Scripts\activate`.
Para regenerar las salidas y los HTML de todas las prácticas:

```bash
python scripts/ejecutar_practicas.py
python investigaciones/ejemplo_knn.py
python create_pdf.py
python scripts/verificar_entrega.py
```

El ejecutor también acepta `--desde 10 --hasta 14`. La preparación de datasets es la práctica 8
y la integración es la 9; deben ejecutarse antes de las que los utilizan. Los CSV preparados ya
se incluyen para consultar cada notebook por separado.

## Datos y reproducibilidad

- [datos_fuente/manifest.json](datos_fuente/manifest.json): descargas de OWID y UCI, URLs, fechas UTC y SHA-256.
- [datos_fuente/material_clase.json](datos_fuente/material_clase.json): archivos de datos previamente proporcionados.
- Cada indicador de OWID conserva su JSON de metadatos, definición y unidad.
- El CSV de Online Retail es un **recorte de clase de 12,786 filas**; no es el dataset UCI completo.
- Los notebooks leen copias locales. Para actualizar fuentes públicas de forma explícita: `python scripts/descargar_datos.py`.

Actualizar fuentes puede modificar cobertura, resultados e interpretaciones. Después de hacerlo
hay que ejecutar de nuevo las prácticas y revisar las conclusiones. Una proyección de 2100 es
un escenario bajo supuestos; no se presenta como una observación futura ni como certeza.

## Fuentes y organización

Las fuentes numéricas son OWID, Naciones Unidas, OMS/Banco Mundial según los metadatos y UCI.
El [repositorio de referencia del curso](https://github.com/No-ly/Big-Data-5to) permitió identificar
el temario y contiene el CSV de clase. Los desarrollos nuevos muestran su procedimiento,
sus propias ejecuciones y las referencias usadas. Se conservaron y ampliaron las prácticas que Jorge ya tenía.

Las carpetas `U1_1_probabilidad_estadistica` y `U3_1_modelos_ml` contienen las prácticas;
`investigaciones` los textos editables; `reportes` los resultados de consulta; `scripts` las herramientas comunes.
El examen original de Jorge se conserva aparte y no forma parte de esta validación de prácticas.
