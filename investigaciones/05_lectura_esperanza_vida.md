# Lectura: esperanza de vida en Estados Unidos y otros países ricos

**Estudiante:** Jorge Adalberto Zuñiga Oliva
**Matrícula:** 82005 · **Grupo:** 512
**Materia:** Tópicos de Big Data
**Fecha de entrega preparada:** 28 de octubre de 2026


## 1. Lectura y pregunta

Se analiza el artículo de Max Roser publicado en 2020 sobre la menor esperanza de vida de Estados
Unidos frente a otros países ricos, pese a su gasto sanitario elevado. El texto discute mortalidad
asociada con tabaco, obesidad, homicidios, sobredosis, suicidios, accidentes e infancia, además de
pobreza y acceso a atención. Sus cifras pertenecen al contexto y fuentes del artículo; no se
presentan aquí como estadísticas actualizadas de 2026.

## 2. Variable objetivo y posibles predictoras

La variable objetivo sería esperanza de vida de periodo al nacer, expresada en años. No es el
promedio aritmético de las edades de quienes murieron. Como candidatas predictoras se podrían
operacionalizar prevalencias, tasas por edad, acceso sanitario, condiciones económicas y gasto.
El artículo motiva hipótesis: no entrega por sí mismo una tabla lista para entrenar ni demuestra
que todas esas columnas constituyan un modelo predictivo validado.

Para construirlo se definiría primero una fila comparable, por ejemplo país-año. Se comprobarían
unidades, cobertura y cambios de definición. El gasto por habitante y el gasto como porcentaje
del PIB son indicadores diferentes; sustituir uno por otro cambia la interpretación. Las tasas
de muerte también pueden formar parte del cálculo del objetivo y causar fuga o circularidad
si la tarea se formula como anticipación antes de observarlas.

## 3. Opinión y variables adicionales

Mi interpretación metodológica es que gasto agregado no basta para explicar resultados sanitarios.
Propondría estudiar contaminación, desigualdad territorial, educación y acceso efectivo, pero como
hipótesis medibles que necesitan fuentes y un diseño. Incluir más columnas sin justificación puede
añadir ruido, sesgo y faltantes. Sería necesario separar asociaciones contemporáneas de predicción
de años posteriores, y reservar datos para evaluar esta última pregunta.

## 4. ¿Todas las variables tendrían el mismo impacto?

No hay razón para imponer efectos iguales. La relación puede variar por edad, país, periodo y
combinación de factores. Coeficientes medidos en unidades distintas no se comparan directamente.
Correlación o importancia de un modelo tampoco prueban causalidad. Para sostener una afirmación
de impacto habría que definir el contraste, atender confusores y justificar el diseño del estudio.

## 5. Conclusión

La lectura ofrece preguntas para investigar, mientras que el ejercicio de datos exige convertirlas
en variables y una evaluación concreta. Un resultado válido debe distinguir definición del objetivo,
disponibilidad de información, asociación y causalidad, además de reconocer qué población representa.

## Referencias

- [Roser, M. (2020). Artículo original en Our World in Data](https://ourworldindata.org/us-life-expectancy-low).
- [OWID: definición y datos de esperanza de vida](https://ourworldindata.org/grapher/life-expectancy).
- [scikit-learn: errores frecuentes y fuga de información](https://scikit-learn.org/stable/common_pitfalls.html).
