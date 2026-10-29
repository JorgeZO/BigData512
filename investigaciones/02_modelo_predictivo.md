# Investigación: qué representa una proyección demográfica

**Estudiante:** Jorge Adalberto Zuñiga Oliva
**Matrícula:** 82005 · **Grupo:** 512
**Materia:** Tópicos de Big Data
**Fecha de entrega preparada:** 28 de octubre de 2026


## 1. Pregunta y fuente

La pregunta es cómo interpretar la esperanza de vida proyectada hasta 2100 que se consulta en OWID.
El indicador utilizado identifica como fuente World Population Prospects 2024 de Naciones Unidas,
con procesamiento de OWID. La fecha final del histórico y la inicial del escenario futuro se leen
de las columnas efectivamente descargadas, no del año actual de la computadora.

## 2. Esperanza de vida de periodo

El indicador sintetiza las tasas de mortalidad por edad de un periodo. Representa cuántos años viviría
una cohorte hipotética sometida a esas tasas durante su vida. No es la media de edades de fallecidos
ni una promesa sobre la duración de vida de una persona. Si las tasas futuras cambian, la experiencia
de una generación real también puede cambiar.

## 3. Modelo demográfico y escenario medio

WPP estima y proyecta población mediante una estructura por edades y componentes demográficos,
considerando fecundidad, mortalidad y migración. No se reduce a una regresión del número de año contra
esperanza de vida. La metodología oficial describe supuestos, datos y proyecciones probabilísticas.
Un escenario central resume una trayectoria condicionada; no elimina la incertidumbre.

Los metadatos del indicador de OWID usado en la práctica describen valores futuros como la media
de miles de trayectorias y explican el tratamiento de 2020-2023 al ajustar la tendencia de mortalidad.
Esa decisión metodológica no significa que se deban borrar años de pandemia de cualquier evaluación:
en nuestros modelos esos años permanecen en la prueba histórica.

## 4. Diferencia con los ejercicios de regresión

Una regresión contra el año aprende una forma funcional a partir de la serie. La lineal prolonga
una pendiente; la cuadrática puede invertir su dirección o producir valores negativos; un bosque
con el año como única entrada termina sin nuevos umbrales fuera del rango observado. Un ajuste
histórico cercano no garantiza una extrapolación demográfica válida.

En el ejercicio de seis variables, la red y la regresión requieren las seis entradas de cada año.
Disponer de una proyección de esperanza de vida no proporciona esas entradas. Se construyen
trayectorias hipotéticas y se informa que sus salidas son escenarios condicionados a esos supuestos.
Las proyecciones externas no se usan como si fueran la verdad para elegir un ganador hasta 2100.

## 5. Conclusión

Antes de interpretar una línea futura hay que preguntar quién la produjo, qué datos observó,
qué supuestos fija, qué periodo representa y qué incertidumbre conserva. La comparación del
repositorio sirve para reconocer límites de modelos simples. No sustituye la metodología de WPP
ni constituye una predicción validada de lo que ocurrirá al final del siglo.

## Referencias

- [Naciones Unidas: WPP 2024, metodología oficial](https://population.un.org/wpp/assets/Files/WPP2024_Methodology-Report_Final.pdf).
- [OWID: esperanza de vida con proyecciones](https://ourworldindata.org/grapher/life-expectancy-at-birth-including-the-un-projections).
- [Metadatos completos del indicador descargado](../datos_fuente/owid/life-expectancy-at-birth-including-the-un-projections.metadata.json).
- [scikit-learn: modelos lineales](https://scikit-learn.org/stable/modules/linear_model.html).
