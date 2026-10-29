# Práctica 9. Dataset integrado de salud e ingreso

**Jorge Adalberto Zuñiga Oliva · 82005 · Grupo 512**

[Notebook completo con código, respuestas y ejecución](../../U3_1_modelos_ml/notebooks/tarea_dataset_health_gdp.ipynb).

## Método y alcance

Se agrega gasto sanitario como porcentaje del PIB y PIB por persona al panel demográfico. La entrega de la tarea conserva exactamente las ocho columnas solicitadas. Otro archivo incorpora esperanza de vida y filtra códigos de tres letras para modelado.

## Resultados

| archivo | filas | entidades |
|---|---|---|
| Tarea: ocho columnas | 4244 | 187 |
| Modelado: seis entradas y objetivo | 4221 | 186 |

## Interpretación

Las fuentes tienen coberturas distintas y las uniones reducen registros. No se rellenan faltantes. Los casos completos pueden sesgar la muestra hacia lugares mejor documentados; se informa cobertura por año para reconocerlo.

Las fuentes, metadatos y decisiones se documentan en el notebook. Los valores de esta tabla se leen de los CSV producidos por su ejecución.
