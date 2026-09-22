# U3_1_modelos_ml — Comparación de modelos de regresión

Práctica de Tópicos de Big Data completada para México. Compara regresión lineal, polinomial de grado 2 y Random Forest para nacimientos y defunciones, entrenando solo con estimaciones históricas de 1950–2023 y proyectando 2024–2100.

## Estructura

```text
U3_1_modelos_ml/
├── data/
│   ├── births-and-deaths-projected-to-2100.csv
│   └── procedencia.json
├── source/
│   └── ejecutar_notebook.py
├── notebook/
│   └── U3_1_modelos_regresion_demografia.ipynb
├── INSTRUCCIONES_Y_RESPUESTAS.md
├── README.md
├── requirements.txt
└── .gitignore
```

El notebook contiene las respuestas junto a sus preguntas, las salidas de ejecución, nueve gráficas y las tablas opcionales. El inventario identifica todas las actividades y las celdas del original que requerían respuestas. El CSV completo se incluye para reproducir también la exploración global de entidades, no únicamente México.

## Consultar y ejecutar

Para revisar la entrega basta abrir el `.ipynb` en GitHub o Jupyter. Para ejecutarla de nuevo, desde esta carpeta, crea un entorno con Python 3.9 o 3.10 e instala las versiones probadas:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python source/ejecutar_notebook.py
```

En Windows, activa el entorno con `.venv\Scripts\activate` en lugar del comando `source`.

El ejecutor usa el Python del entorno activo, ejecuta todas las celdas en orden y actualiza el notebook con sus salidas solo si termina sin errores. También puedes abrirlo con `python -m jupyterlab` y elegir «Restart Kernel and Run All Cells». Selecciona el kernel del entorno con las dependencias instaladas. La carga funciona desde `U3_1_modelos_ml` o su subcarpeta `notebook`.

Las bibliotecas requieren conexión para instalarse. Una vez instaladas, el notebook utiliza el CSV local y no necesita descargar datos. Si eliminas el CSV, la celda de carga intenta descargarlo; una nueva versión de OWID podría cambiar los resultados o el corte histórico y las comprobaciones te avisarán.

## Resultados y límites

- Hay 74 registros históricos y 77 proyectados para México; no faltan valores en las variables de entrenamiento.
- La regresión lineal de nacimientos llega a unos 3.14 millones en 2100, aunque los nacimientos recientes descienden.
- La polinomial representa la curvatura histórica, pero produce nacimientos negativos desde 2058.
- Random Forest da valores futuros constantes con el año como única variable predictora.
- Ningún modelo reproduce adecuadamente ambas curvas de OWID durante todo el horizonte. Concordar con OWID no equivale a predecir el futuro observado.
- No se calculan métricas, de acuerdo con la consigna: la evaluación formal corresponde a la próxima práctica.

## Fuentes y reproducibilidad

Datos de [Our World in Data: Births and deaths](https://ourworldindata.org/grapher/births-and-deaths-projected-to-2100), basados en estimaciones y proyecciones de Naciones Unidas. El escenario de proyección es el medio. La URL exacta, fecha UTC de descarga y SHA-256 del CSV se conservan en `data/procedencia.json`. Mantén esta atribución al compartirlo; consulta en OWID los términos aplicables a los datos de terceros.

La explicación de extrapolación de los árboles se apoya en la [documentación oficial de scikit-learn](https://scikit-learn.org/stable/modules/tree.html). Se conserva `random_state=42` y 100 árboles del original. Las versiones directas empleadas se especifican en `requirements.txt`; la ejecución se verificó con Python 3.9.6.

## Entrega en GitHub

Sube la carpeta completa `U3_1_modelos_ml` a tu repositorio. Verifica que el notebook muestre preguntas, respuestas y gráficas, y entrega el enlace del repositorio o de esta carpeta según lo que solicite el docente. No subas el entorno `.venv`. Esta preparación no crea ni publica un repositorio remoto.
