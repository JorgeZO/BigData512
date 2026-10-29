# Resumen de resultados: regresión demográfica de México

**Estudiante:** Jorge Adalberto Zuñiga Oliva
**Matrícula:** 82005 · **Grupo:** 512
**Materia:** Tópicos de Big Data
**Fecha de entrega preparada:** 28 de octubre de 2026


## 1. Pregunta y datos

Se comparan lineal, cuadrática y Random Forest en nacimientos y defunciones de México (OWID/ONU).
La prueba reserva 2014-2023 después de entrenar con 1950-2013. Las curvas 2024-2100 son
escenarios externos y extrapolaciones, no observaciones de evaluación.

## 2. Modelos y resultados en prueba

La lineal obliga a una tendencia recta. La cuadrática tiene más flexibilidad y también mayor
riesgo al prolongarse. El bosque aproxima tramos aprendidos y no continúa automáticamente una
tendencia fuera del rango del año. Persistencia repite el último conteo de 2013 y sirve como base.

| Variable | Modelo | MAE | RMSE |
|---|---|---:|---:|
| births | Persistencia | 184,644 | 195,852 |
| births | Lineal | 567,421 | 576,894 |
| births | Polinomial 2 | 131,460 | 139,979 |
| births | Random Forest | 184,407 | 195,629 |
| deaths | Persistencia | 150,020 | 213,195 |
| deaths | Lineal | 247,818 | 289,384 |
| deaths | Polinomial 2 | 87,502 | 159,515 |
| deaths | Random Forest | 162,724 | 222,317 |

En esta ventana, la cuadrática tiene el menor MAE para ambas variables entre las configuraciones
probadas. El resultado no implica que sea el mejor modelo hasta 2100. Comparar solo un ajuste
de entrenamiento habría ocultado errores de generalización y omitido la referencia de persistencia.

## 3. Lectura de las proyecciones

Una curva puede ajustarse al pasado y extrapolar valores poco plausibles. Las predicciones negativas
se conservan como evidencia de ese límite. El bosque aplana su respuesta cuando los años futuros
quedan fuera de sus últimos umbrales aprendidos.

OWID/ONU usa una metodología demográfica diferente. Parecerse a su curva no valida los modelos:
sería comparar dos estimaciones del futuro. La evaluación requiere observaciones reservadas.

## 4. Conclusión

Flexibilidad, ajuste histórico y extrapolación son distintos. La cuadrática gana en esta ventana,
pero no queda validada hasta 2100. MAE y RMSE se informan en eventos por año; la pandemia y
los cambios de estructura poblacional limitan la comparación.

## Referencias

[OWID: nacimientos y defunciones](https://ourworldindata.org/grapher/births-and-deaths-projected-to-2100) · [scikit-learn: regresión lineal](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html).

[scikit-learn: RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) · [Métricas calculadas en la práctica](../U3_1_modelos_ml/data/processed/U3_1_metricas_mexico.csv).
