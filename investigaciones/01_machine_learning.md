# Investigación: preparación, modelos y evaluación de Machine Learning

**Estudiante:** Jorge Adalberto Zuñiga Oliva
**Matrícula:** 82005 · **Grupo:** 512
**Materia:** Tópicos de Big Data
**Fecha de entrega preparada:** 28 de octubre de 2026


## 1. Preparación de datos

El primer paso es definir la unidad de observación y la pregunta. En el repositorio, una fila puede
ser un país-año, un cliente o una línea de factura. Mezclar esas unidades cambia el significado del
resultado, incluso si el código se ejecuta correctamente. Conviene registrar fuente, fecha, unidades,
diccionario de columnas y llaves antes de entrenar.

### Limpieza, faltantes y duplicados

La limpieza revisa tipos, rangos, etiquetas, fechas y registros repetidos. Un duplicado de llave puede
multiplicar filas al hacer merge; una línea de venta idéntica podría ser un duplicado o una compra real.
La decisión debe justificarse. El informe de limpieza registra cuántas filas quedan tras cada filtro.

Un dato ausente no siempre significa cero. Se puede eliminar una observación si impide el análisis,
imputar con una regla estimada en entrenamiento o conservar un indicador de ausencia. Imputar con
la media de toda la tabla antes de separar prueba filtra información. En el panel de este trabajo se
usan casos completos y se reconoce que eso limita la cobertura geográfica y temporal.

### Valores atípicos

Un extremo puede ser un error de captura o un evento válido. Se inspeccionan distribución, unidades
y contexto antes de borrarlo. En las compras se retienen importes altos; logaritmos reducen su peso
relativo. Recortar sin justificación puede eliminar justamente clientes o crisis que interesa estudiar.

### Transformación, normalización y categorías

StandardScaler calcula (x - media) / desviación. Min-Max usa los extremos para llevar el rango observado
a [0, 1]. Ninguno produce automáticamente una distribución normal. log1p(x) admite cero y comprime
valores grandes. Cada transformación debe corresponder a su dominio: ln(x) requiere valores positivos.

Las categorías nominales pueden representarse con one-hot, cuidando categorías desconocidas en prueba.
Asignar números a países o clientes no crea una distancia con significado. En clustering de gastos,
Channel y Region quedan fuera de las seis coordenadas de gasto y se pueden usar para describir grupos.

### Selección de variables, X e y

X contiene información disponible al aplicar el modelo; y es la respuesta en aprendizaje supervisado.
No se debe incluir una variable que revele directamente el resultado ni información conocida después
del instante de predicción. Escoger variables mirando repetidamente el resultado de prueba también
contamina la evaluación. En la práctica de esperanza de vida se declara que las seis entradas son
del mismo año: el resultado es una estimación condicionada, no un pronóstico previo a conocerlas.

## 2. Tipos de problemas y seis modelos

En aprendizaje supervisado existen respuestas de entrenamiento. Clasificación devuelve categorías o
probabilidades; regresión estima cantidades. En aprendizaje no supervisado se busca estructura sin
una respuesta conocida. Clustering describe grupos y necesita evaluación acorde con ese objetivo.

| Modelo | Problema habitual | Idea y cuidado principal |
|---|---|---|
| Regresión lineal | Regresión | Ajusta una suma ponderada de entradas; extrapolar una recta puede ser inadecuado. |
| Regresión logística | Clasificación | Modela probabilidades de clase; el umbral debe corresponder al costo de los errores. |
| Árbol de decisión | Clasificación o regresión | Divide el espacio con reglas; profundidad excesiva puede memorizar datos. |
| KNN | Clasificación o regresión | Consulta observaciones cercanas; escala y distancia cambian quién es vecino. |
| Random Forest | Clasificación o regresión | Combina árboles para reducir inestabilidad; no garantiza extrapolar tendencias. |
| K-Means | Clustering | Alterna asignación y centroides; exige elegir k y una geometría con sentido. |

En el bosque, bootstrap y selección aleatoria de variables son mecanismos configurables. No es correcto
afirmar que todos los parámetros por defecto de regresión usan necesariamente un subconjunto estricto
de columnas en cada división. Se documentan los parámetros usados, en lugar de inferirlos del nombre.

## 3. Entrenamiento, validación, prueba y generalización

Entrenamiento ajusta parámetros; validación ayuda a escoger decisiones; prueba se reserva para estimar
desempeño después de fijarlas. Una Pipeline permite volver a ajustar el preprocesamiento dentro de
cada partición de validación. En series temporales se respeta el orden: entrenar con años posteriores
y probar en años anteriores responde otra pregunta. Un corte temporal puede seguir incluyendo los
mismos países; no equivale a una prueba en países nuevos.

Sobreajuste significa capturar peculiaridades que no se sostienen fuera del entrenamiento. Subajuste
significa que la familia elegida no representa una estructura útil. Se comparan errores y curvas en
conjuntos adecuados; una buena apariencia visual en entrenamiento no basta.

## 4. Evaluación según la pregunta

En clasificación binaria, una matriz de confusión separa verdaderos/falsos positivos y negativos.
Accuracy es la proporción de aciertos; precisión mide cuántos positivos predichos eran positivos;
recall mide cuántos positivos reales se detectaron. F1 combina precisión y recall. El promedio macro
da igual peso a cada clase. El resultado debe acompañarse de prevalencia y una línea base.

En regresión, MAE promedia errores absolutos; RMSE penaliza más los errores grandes y conserva la
unidad del objetivo. R2 compara con una referencia basada en la media y puede ser negativo en prueba.
No es un porcentaje de causalidad ni prueba de validez futura. Se contrasta también con persistencia
cuando la pregunta tiene orden temporal.

En K-Means, la inercia disminuye al agregar grupos y por eso no basta para elegir k. La silueta
compara cohesión y separación. Ni una puntuación alta ni un grupo pequeño garantizan utilidad:
se revisan perfiles, tamaños, estabilidad y la unidad que está siendo segmentada.

## 5. Aplicación al repositorio

Los datos públicos se guardan con URL, metadatos y SHA-256. Los notebooks muestran llaves, faltantes,
criterios de limpieza, transformaciones, resultados y límites. En regresión demográfica se reserva
2014-2023; en el panel de seis entradas se reserva 2018-2022. Los escenarios de 2100 declaran sus
supuestos y no se presentan como observaciones. En ventas, los porcentajes distinguen clientes de líneas.

## Referencias

[scikit-learn: imputación](https://scikit-learn.org/stable/modules/impute.html) · [scikit-learn: preprocesamiento](https://scikit-learn.org/stable/modules/preprocessing.html) · [scikit-learn: modelos lineales y logística](https://scikit-learn.org/stable/modules/linear_model.html).

[scikit-learn: árboles](https://scikit-learn.org/stable/modules/tree.html) · [scikit-learn: ensambles](https://scikit-learn.org/stable/modules/ensemble.html) · [scikit-learn: vecinos](https://scikit-learn.org/stable/modules/neighbors.html).

[scikit-learn: validación](https://scikit-learn.org/stable/modules/cross_validation.html) · [scikit-learn: métricas](https://scikit-learn.org/stable/modules/model_evaluation.html) · [scikit-learn: errores frecuentes](https://scikit-learn.org/stable/common_pitfalls.html).
