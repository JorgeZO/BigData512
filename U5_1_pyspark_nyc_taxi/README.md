# U5.1 - Preparación local de PySpark y NYC Taxi

Jorge Adalberto Zuñiga Oliva · Matrícula 82005 · Grupo 512.

El notebook conserva las seis celdas de código de la práctica proporcionada y agrega
una celda de configuración local, respuestas de reflexión y cierre de recursos. Trabaja con una muestra de 1,000 viajes
de Yellow Taxi de enero de 2025. PyArrow consulta tres columnas del primer grupo de filas
del Parquet por HTTP; Spark procesa la muestra en esta computadora mediante `local[*]`.
Las primeras filas no constituyen una muestra aleatoria representativa del mes.

## Entorno

- Python 3.12.
- Java 17, mediante `JAVA_HOME`.
- Dependencias fijadas en [requirements.txt](requirements.txt).

En esta Mac, `.venv` ya está creado. Desde esta carpeta:

```bash
source .venv/bin/activate
python ejecutar_preparacion.py
```

Para preparar otra computadora con Python 3.12 y Java 17 disponibles:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Seleccionar `.venv/bin/python` como kernel en VS Code. El entorno de esta Mac utiliza un
JDK aislado cuya ruta está en `.runtime-local.json`, archivo ignorado por Git. El ejecutor
aplica esa configuración solo al proceso de la práctica. La primera celda de código también
la carga al usar Run All en VS Code, de modo que el kernel utilice este Java y su mismo Python
para los procesos de Spark.

```bash
python ejecutar_preparacion.py
```

El ejecutor lee todo el notebook, detiene la ejecución ante un error y, únicamente si
termina correctamente, guarda el notebook con sus resultados, una exportación HTML y
`evidencia/ejecucion_local.json` con versiones, fecha y huella del archivo.

## Evidencia de la ejecución

- [Notebook ejecutado](notebooks/U5_1_preparation_pyspark_NYC_taxi.ipynb).
- [Resultado HTML](evidencia/U5_1_preparation_pyspark_NYC_taxi.html).
- [Versiones, conteos y huella](evidencia/ejecucion_local.json).

## GitHub y Databricks

Las dependencias de este entorno son locales. En Databricks se utiliza el cómputo de
la plataforma y una Git folder del repositorio `JorgeZO/BigData512` para sincronizar cambios.
El archivo `sincronizacion_git.txt` se utiliza para comprobar el recorrido Git local,
GitHub y Databricks sin modificar datos ni tablas.

## Fuentes

- [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
- [Archivo Parquet de enero de 2025](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet).
- [Instalación de PySpark 4.0.1](https://spark.apache.org/docs/4.0.1/api/python/getting_started/install.html).
- [Databricks: conectar GitHub](https://docs.databricks.com/aws/en/repos/get-access-tokens-from-git-provider).
- [Databricks: pull, commit y push](https://docs.databricks.com/aws/en/repos/git-operations-with-repos).
