from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_pdf():
    pdf_path = r"C:\Users\Santiago\Desktop\Escuela\5to Semestre ISSC\BigData\Resumen_Modelos_Regresion.pdf"
    
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = styles['Heading1']
    title_style.alignment = 1  # Center
    subtitle_style = styles['Heading2']
    body_style = styles['BodyText']
    body_style.spaceAfter = 12
    
    Story = []
    
    # Title
    Story.append(Paragraph("Resumen de Práctica: Comparación de Modelos de Regresión", title_style))
    Story.append(Spacer(1, 12))
    
    # Introduction
    Story.append(Paragraph("Objetivo de la Práctica", subtitle_style))
    Story.append(Paragraph(
        "El objetivo principal fue construir y comparar diferentes modelos de aprendizaje supervisado (Machine Learning) "
        "para proyectar la cantidad de nacimientos y defunciones de Japón hacia el futuro (año 2100). "
        "Se utilizaron datos demográficos históricos de Our World In Data (OWID), donde la variable predictora "
        "fue el 'Año' y la variable objetivo fue la cantidad de nacimientos o defunciones.", body_style))
    
    # Regresión Lineal
    Story.append(Paragraph("1. Regresión Lineal", subtitle_style))
    Story.append(Paragraph(
        "¿Qué se hizo? Se entrenó un modelo LinearRegression utilizando los datos históricos. Este modelo asume "
        "que existe una relación constante (una línea recta) entre el avance de los años y el número de eventos demográficos.", body_style))
    Story.append(Paragraph(
        "Resultados: Al graficar los resultados, se observó que la recta de regresión lineal no puede capturar las "
        "variaciones reales (picos y valles) de los datos de Japón. En las proyecciones a largo plazo (año 2100), "
        "el modelo tiende a subestimar drásticamente los datos, sugiriendo valores que pueden llegar a ser negativos, lo cual "
        "carece de sentido biológico y demográfico.", body_style))
    
    # Regresión Polinomial
    Story.append(Paragraph("2. Regresión Polinomial", subtitle_style))
    Story.append(Paragraph(
        "¿Qué se hizo? Se aplicó una transformación PolynomialFeatures de grado 2 a la variable predictora antes "
        "de aplicar regresión lineal. Esto permitió que el modelo trazara una curva en lugar de una recta.", body_style))
    Story.append(Paragraph(
        "Resultados: El ajuste a los datos históricos fue visualmente excelente, logrando capturar la curva en "
        "forma de 'montaña' de los nacimientos. Sin embargo, su principal desventaja se hizo evidente en la "
        "extrapolación hacia el futuro: la función parabólica cae bruscamente hacia el infinito negativo. En el año 2100, "
        "las predicciones resultaron en valores absurdos (millones en números negativos), demostrando que extrapolar polinomios "
        "a largo plazo es muy peligroso.", body_style))
    
    # Random Forest Regressor
    Story.append(Paragraph("3. Random Forest Regressor", subtitle_style))
    Story.append(Paragraph(
        "¿Qué se hizo? Se entrenó un algoritmo basado en múltiples árboles de decisión (ensamblaje). "
        "Estos modelos fragmentan los datos y calculan promedios sobre segmentos históricos.", body_style))
    Story.append(Paragraph(
        "Resultados: En los datos de entrenamiento (históricos), el modelo sobreajustó (overfitting) la serie "
        "trazando una línea casi idéntica a los datos reales. El problema surgió en la proyección después de 2023: "
        "la curva se volvió completamente plana. Random Forest no es capaz de predecir valores fuera del rango "
        "numérico con el que fue entrenado, por lo que su capacidad de pronosticar tendencias futuras a largo "
        "plazo fue nula.", body_style))

    # Conclusión
    Story.append(Paragraph("Conclusión General", subtitle_style))
    Story.append(Paragraph(
        "La práctica evidenció los riesgos de utilizar algoritmos de regresión matemáticos puros para predecir series "
        "de tiempo complejas a largo plazo (extrapolación). Cada modelo mostró limitaciones graves al proyectar hacia el año 2100. "
        "Para realizar proyecciones demográficas útiles, es necesario usar sistemas especializados como los de la ONU, que "
        "contemplan la estructura por edades, fertilidad, y aspectos sociales, y no solo ajustar funciones estadísticas al pasado.", body_style))

    # Build the document
    doc.build(Story)

if __name__ == '__main__':
    create_pdf()
