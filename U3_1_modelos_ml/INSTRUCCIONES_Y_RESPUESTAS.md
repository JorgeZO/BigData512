# Inventario de instrucciones y pendientes del original

Numeración de celdas **desde 1**, contando código y texto. Se conservan las 104 celdas originales y su orden. Los identificadores internos `original-000` empiezan en cero.

El original contiene 53 celdas de código y 51 de texto. No hay celdas de código vacías, TODO ni bloques de implementación omitidos. Se deben ejecutar y analizar todas las celdas de código. Las respuestas explícitas y observaciones pendientes están en las celdas **13, 28, 60, 73, 84 y 103**; la celda **21** pide identificar variables. En total son siete celdas con trabajo escrito, incluyendo esa identificación.

## Todas las preguntas y observaciones pendientes

### Celda 13

### Pregunta

**¿Cuál es la unidad de observación de cada fila del dataset?**

*(Escribe tu respuesta aquí)*



### Celda 21

## 7. Revisar las variables disponibles

Identifica las columnas correspondientes a: **año**, **nacimientos** y **defunciones**.

### Celda 28

### Preguntas de observación

1. ¿Los nacimientos presentan una tendencia constante?
2. ¿Las defunciones presentan una tendencia constante?
3. ¿Las dos variables parecen seguir el mismo comportamiento?
4. ¿Observas cambios en la tendencia a través del tiempo?

*(Escribe tus observaciones aquí)*

### Celda 60

### Observación

Analiza cómo continúa la tendencia histórica cuando utilizamos una **función lineal**. ¿Qué pasa con los valores hacia el año 2100?

### Celda 73

### Observación

Compara el comportamiento de esta gráfica con el modelo de regresión lineal. ¿Se ajusta mejor a los datos históricos? ¿Qué ocurre con la proyección hacia el año 2100? ¿Los valores que predice tienen sentido para un número de nacimientos?

### Celda 84

### Observación

Fíjate en dos cosas: (1) qué tan bien sigue el modelo los datos históricos y (2) qué sucede con la línea después de 2023. ¿Continúa la tendencia? ¿Por qué crees que sucede esto? Investiga.

### Celda 103

# PARTE 17. Reflexión

Responde las siguientes preguntas en esta misma celda (haz doble clic para editarla).

### 1.
¿Qué diferencia observaste entre la regresión lineal, la regresión polinomial y Random Forest?

*Respuesta:*

### 2.
¿Por qué los tres modelos generan predicciones diferentes si utilizaron los mismos datos históricos?

*Respuesta:*

### 3.
¿Qué modelo produjo una tendencia más cercana visualmente a las proyecciones de OWID?

*Respuesta:*

### 4.
¿El modelo que visualmente parece acercarse más a las proyecciones de OWID necesariamente es el mejor modelo? Explica.

*Respuesta:*

### 5.
¿Qué comportamiento observaste en las predicciones de Random Forest para los años posteriores a 2023?

*Respuesta:*

### 6.
¿Por qué debemos tener cuidado al utilizar un modelo entrenado con datos históricos para realizar predicciones hasta el año 2100?

*Respuesta:*

## Actividades de ejecución y análisis

| Parte / celdas originales | Instrucción y evidencia esperada |
|---|---|
| Introducción / 1 | Comparar regresión lineal, polinomial y Random Forest para nacimientos y defunciones; no evaluar todavía mediante métricas. |
| 1 / 2–4 | Importar Pandas, NumPy, Matplotlib y los tres estimadores/transformadores. |
| 2 / 5–17 | Cargar OWID, explorar dimensiones, tipos, columnas y entidades; responder unidad de observación; renombrar columnas, conservar copia y unificar estimaciones/proyecciones. |
| 3 / 18–23 | Seleccionar México, revisar años y filas e identificar Year, births y deaths. |
| 4 / 24–28 | Graficar nacimientos y defunciones y responder las cuatro preguntas de observación. |
| 5 / 29–35 | Verificar corte histórico/proyectado, separar hasta 2023 y desde 2024 y revisar faltantes. |
| 6 / 36–43 | Definir X e y, convertir a NumPy y observar formas (74, 1) y (74,). |
| 7 / 44–57 | Crear y entrenar regresión lineal, inspeccionar coeficientes, predecir histórico y 2024–2100 usando nombres de columnas coherentes. |
| 8 / 58–60 | Graficar el ajuste y proyección lineales; explicar qué ocurre en 2100. |
| 9 / 61–70 | Crear términos de grado 2, entrenar regresión polinomial, predecir histórico y futuro con el mismo transformador. |
| 10 / 71–73 | Graficar y comparar ajuste histórico, proyección a 2100 y plausibilidad de nacimientos. |
| 11 / 74–81 | Entrenar Random Forest con 100 árboles y semilla 42 y generar predicciones históricas y futuras. |
| 12 / 82–84 | Graficar Random Forest, comentar ajuste histórico y comportamiento posterior a 2023 e investigar su explicación. |
| 13 / 85–86 | Comparar los tres modelos de nacimientos; limitar eje vertical es opcional. Se conserva el rango completo para mostrar valores negativos. |
| 14 / 87–94 | Repetir los tres modelos cambiando el objetivo a defunciones. |
| 15 / 95–96 | Comparar gráficamente las tres proyecciones de defunciones. |
| 16 / 97–102 | Comparar ambos objetivos con OWID; elaborar también el resumen numérico opcional para 2030, 2050, 2075 y 2100. |
| 17 / 103 | Contestar las seis preguntas finales en la misma celda. |
| 18 / 104 | Reconocer los ocho conceptos del glosario y distinguir ajuste, predicción y extrapolación. |

## Instrucción externa de entrega

Crear `U3_1_modelos_ml/data`, `source` y `notebook`, colocar el notebook en `notebook` y, una vez concluido, subir esa carpeta a un repositorio de GitHub y entregar su enlace. La publicación requiere el repositorio del alumno; esta entrega prepara los archivos y no publica un repositorio.

## Versión publicada

Se publica el archivo del alumno `U3_1_modelos_regresion_demografia (1).ipynb` sin modificar su contenido. El inventario anterior describe las actividades del original. Esta versión conserva su carga por internet y su alternativa local en la carpeta del notebook; no incorpora las comprobaciones añadidas a la versión anterior. La tabla opcional tiene un error guardado, documentado en README.
