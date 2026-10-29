# Investigación: K-Nearest Neighbors (KNN)

**Estudiante:** Jorge Adalberto Zuñiga Oliva
**Matrícula:** 82005 · **Grupo:** 512
**Materia:** Tópicos de Big Data
**Fecha de entrega preparada:** 28 de octubre de 2026


## 1. Principio

KNN predice a partir de ejemplos cercanos a una consulta. En clasificación combina etiquetas;
en regresión combina valores numéricos. Es un método no paramétrico: no presupone una recta
para la relación entre entradas y respuesta. Al ajustar conserva datos y puede construir una
estructura de búsqueda; el trabajo de localizar vecinos se realiza al consultar.

## 2. Procedimiento y ejemplo manual

Primero se define X, y y la partición de evaluación. Después se ajusta el preprocesamiento solo con
entrenamiento, se eligen k y una distancia mediante validación, y se consultan los k vecinos.
Con voto uniforme gana la clase más frecuente; con ponderación, los vecinos no aportan el mismo peso.

Considérense A=(0,0), A=(0,2), B=(3,0) y B=(3,2). Para la consulta (1,1), las dos distancias
a A son sqrt(2) y las dos distancias a B son sqrt(5). Con k=3, dos vecinos son A y uno es B:
el voto uniforme predice A. La distancia por sí misma no es una probabilidad de pertenencia.

## 3. Distancia y preparación

La distancia euclidiana es la raíz de la suma de diferencias al cuadrado. Manhattan suma valores
absolutos; Minkowski generaliza ambas con un parámetro. La elección depende de las variables.
Si una coordenada está en millones y otra en unidades, la primera puede dominar: se escala cuando
eso corresponde a la pregunta. Si los atributos ya están en unidades comparables, escalar sigue
siendo una decisión metodológica y no una regla universal automática.

Los faltantes requieren una estrategia previa. Categorías nominales necesitan representación
adecuada; números de identificación no expresan semejanza. Un logaritmo puede ayudar con
asimetría, pero cambia la geometría. Se debe aplicar la misma transformación a consulta y entrenamiento.

## 4. Elegir k sin mirar prueba

k pequeño produce decisiones locales sensibles al ruido. k grande suaviza y puede perder grupos
minoritarios. Se comparan valores con validación cruzada y una métrica adecuada, manteniendo
el conjunto de prueba reservado. La Pipeline vuelve a ajustar StandardScaler dentro de cada
fold, evitando que las medias del fold de validación entren en el preprocesamiento.

## 5. Variantes, costo y dimensión

KNeighborsClassifier y KNeighborsRegressor usan voto y promedio, respectivamente. Se puede
ponderar por distancia o definir un radio en vez de un número fijo. NearestNeighbors solo busca
ejemplos similares y no necesita etiquetas. Búsquedas por fuerza bruta comparan la consulta con
muchos registros; estructuras de árboles pueden acelerar ciertos casos.

En alta dimensión aumentan el costo y los problemas de representación de distancias. Variables
irrelevantes pueden hacer menos útil la noción de cercanía. Reducir columnas exige validar de nuevo:
no toda reducción preserva lo necesario para predecir. La memoria depende del entrenamiento conservado.

## 6. KNN y K-Means

| Aspecto | KNN supervisado | K-Means |
|---|---|---|
| Uso de respuestas y | Sí | No |
| Significado de k | Número de vecinos de una consulta | Número de grupos |
| Resultado | Clase o valor de una consulta | Etiquetas y centroides |
| Evaluación | Métricas sobre respuestas reservadas | Separación, cohesión, estabilidad y utilidad |

La consulta de vecinos del ejercicio mayorista utiliza NearestNeighbors. No debe describirse
como clasificación KNN, porque no se predice una etiqueta conocida.

## 7. Implementación y resultados reproducibles

El archivo `ejemplo_knn.py` usa Iris incluido en scikit-learn. Reserva 30% para prueba, estratifica
por especie y selecciona k entre 1, 3, 5, 7, 9 y 11 mediante cinco folds en el 70% restante.
StandardScaler y KNN forman una Pipeline; se fija semilla 82005. Para reproducir:

```bash
python investigaciones/ejemplo_knn.py
```

En la ejecución, k=5; F1 macro medio de validación=0.9713. En prueba, accuracy=0.9556 y F1 macro=0.9554.

Filas de la matriz = clase real; columnas = predicción. Orden: setosa, versicolor, virginica.

| Real / predicha | setosa | versicolor | virginica |
|---|---:|---:|---:|
| setosa | 15 | 0 | 0 |
| versicolor | 0 | 13 | 2 |
| virginica | 0 | 0 | 15 |

El conjunto de prueba tiene solo 45 ejemplos. Este resultado describe una partición de un dataset
pequeño; no garantiza desempeño en otras flores, variables o poblaciones. Las clases confundidas
se observan en la matriz y no deben ocultarse mostrando solo accuracy.

## 8. Conclusión

KNN es fácil de formular, pero una solución completa exige justificar representación, escala,
distancia, k, costo y evaluación. Puede servir como línea base y para comparar observaciones
similares. No convierte cercanía en causalidad ni reemplaza la comprobación en datos reservados.

## Referencias

- [scikit-learn: guía de vecinos cercanos](https://scikit-learn.org/stable/modules/neighbors.html).
- [scikit-learn: KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).
- [scikit-learn: GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html).
- [scikit-learn: Iris y su referencia original](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html).
- [scikit-learn: matriz de confusión](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html).
