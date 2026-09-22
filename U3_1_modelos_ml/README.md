# U3_1_modelos_ml — Modelos de regresión demográfica

La versión entregada es una copia exacta de `U3_1_modelos_regresion_demografia (1).ipynb`, proporcionada por el alumno, guardada con el nombre solicitado dentro de `notebook`. Contiene las respuestas de observación y las seis reflexiones finales. Sustituye la versión preparada anteriormente.

## Estructura

- `notebook/U3_1_modelos_regresion_demografia.ipynb`: notebook del alumno con sus salidas guardadas.
- `data/`: CSV de OWID y registro de procedencia.
- `source/ejecutar_notebook.py`: ejecutor opcional para volver a generar las salidas.
- `requirements.txt`: dependencias del entorno usado para preparar la entrega anterior.
- `INSTRUCCIONES_Y_RESPUESTAS.md`: inventario de actividades del ejercicio.

## Ejecución

Para consultar las respuestas, abre el notebook en GitHub o Jupyter. Para ejecutarlo, instala las dependencias con `python -m pip install -r requirements.txt` y abre el notebook con Jupyter. El código del alumno intenta descargar OWID primero; si no hay conexión, busca el CSV en la misma carpeta del notebook. En ese caso, copia temporalmente el CSV de `data` a `notebook`.

El archivo se conserva sin modificaciones. Su celda final de código (resumen numérico opcional, celda 102) contiene una salida guardada con `AttributeError`; por ello esta versión no se presenta como una ejecución íntegra sin errores. Las respuestas finales sí están presentes y separadas por pregunta.

## Fuente

[Our World in Data — Births and deaths](https://ourworldindata.org/grapher/births-and-deaths-projected-to-2100), basado en estimaciones y proyecciones de Naciones Unidas. La URL y huella del CSV incluido se encuentran en `data/procedencia.json`.
