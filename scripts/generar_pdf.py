"""Renderiza textos y reportes en PDF y reúne un portafolio con marcadores."""
from io import BytesIO
from pathlib import Path
import argparse
import html
import re
from urllib.parse import quote
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, Preformatted
from pypdf import PdfWriter

RAIZ = Path(__file__).resolve().parents[1]
ANCHO = 512
AZUL = colors.HexColor("#163e55")
ESTILOS = {
    "titulo": ParagraphStyle("titulo", fontName="Helvetica-Bold", fontSize=19, leading=23, textColor=AZUL, spaceAfter=13),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=AZUL, spaceBefore=9, spaceAfter=6, keepWithNext=True),
    "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=AZUL, spaceBefore=10, spaceAfter=6, keepWithNext=True),
    "cuerpo": ParagraphStyle("cuerpo", fontName="Helvetica", fontSize=9.2, leading=12, spaceAfter=5, splitLongWords=True),
    "tabla": ParagraphStyle("tabla", fontName="Helvetica", fontSize=7.5, leading=10, splitLongWords=True),
    "cabecera": ParagraphStyle("cabecera", fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=colors.white),
    "codigo": ParagraphStyle("codigo", fontName="Courier", fontSize=8, leading=11, leftIndent=9, spaceBefore=5, spaceAfter=9),
}


def normalizar(s):
    return str(s).translate(str.maketrans({"—": "-", "–": "-", "−": "-", "→": "->", "≥": ">=", "≤": "<=", "×": "x", "’": "'", "“": '"', "”": '"'}))


def inline(texto, origen):
    texto = html.escape(normalizar(texto))
    def enlace(m):
        etiqueta, destino = m.groups()
        if not destino.startswith(("https://", "http://")):
            relativo = (origen.parent / html.unescape(destino)).resolve().relative_to(RAIZ)
            destino = "https://github.com/JorgeZO/BigData512/blob/main/" + quote(relativo.as_posix())
        return f'<a href="{html.escape(destino, quote=True)}" color="#146c94">{etiqueta}</a>'
    texto = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", enlace, texto)
    texto = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto)
    return re.sub(r"`([^`]+)`", r'<font face="Courier">\1</font>', texto)


def tabla_pdf(lineas, origen):
    filas = [[c.strip() for c in linea.strip().strip("|").split("|")] for linea in lineas]
    filas = [f for f in filas if not all(re.fullmatch(r"[: -]+", c) for c in f)]
    cantidad = len(filas[0])
    if any(len(f) != cantidad for f in filas): raise ValueError(f"Tabla inválida: {origen}")
    pesos = [max(8, min(32, max(len(re.sub(r"`|\*", "", f[i])) for f in filas))) for i in range(cantidad)]
    datos = [[Paragraph(inline(c, origen), ESTILOS["cabecera" if j == 0 else "tabla"]) for c in f] for j, f in enumerate(filas)]
    tabla = Table(datos, colWidths=[ANCHO*p/sum(pesos) for p in pesos], repeatRows=1, hAlign="LEFT", spaceBefore=5, spaceAfter=12)
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), AZUL),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#f1f5f7"), colors.white]),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LINEBELOW", (0,-1), (-1,-1), .4, colors.HexColor("#c8d4db")),
    ]))
    return tabla


def elementos(texto, origen):
    lineas, flujo, i = texto.splitlines(), [], 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if not linea:
            i += 1; continue
        if linea.startswith("```"):
            codigo = []; i += 1
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                codigo.append(normalizar(lineas[i])); i += 1
            flujo.append(Preformatted("\n".join(codigo), ESTILOS["codigo"]))
        elif linea.startswith("|"):
            tabla = []
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                tabla.append(lineas[i]); i += 1
            flujo.append(tabla_pdf(tabla, origen)); continue
        elif linea.startswith("!["):
            m = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", linea)
            if not m: raise ValueError(linea)
            imagen = Image(str((origen.parent/m.group(2)).resolve()))
            escala = min(ANCHO/imagen.imageWidth, 210/imagen.imageHeight)
            imagen.drawWidth, imagen.drawHeight = imagen.imageWidth*escala, imagen.imageHeight*escala
            flujo.extend([imagen, Paragraph(inline(m.group(1), origen), ESTILOS["tabla"]), Spacer(1,10)])
        elif linea.startswith("#"):
            nivel = len(linea)-len(linea.lstrip("#"))
            estilo = "titulo" if nivel == 1 else "h2" if nivel == 2 else "h3"
            flujo.append(Paragraph(inline(linea.lstrip("# "), origen), ESTILOS[estilo]))
        else:
            partes = [linea]; i += 1
            while i < len(lineas) and lineas[i].strip() and not lineas[i].lstrip().startswith(("#", "|", "```", "![", "- ")):
                partes.append(lineas[i].strip()); i += 1
            es_lista = partes[0].startswith("- ")
            cuerpo = " ".join(partes)
            flujo.append(Paragraph(inline(cuerpo[2:] if es_lista else cuerpo, origen), ESTILOS["cuerpo"], bulletText="•" if es_lista else None))
            continue
        i += 1
    return flujo


def pagina(canvas, doc):
    canvas.saveState(); canvas.setStrokeColor(colors.HexColor("#bfd1dc")); canvas.line(50,751,562,751)
    canvas.setFont("Helvetica",8); canvas.setFillColor(colors.HexColor("#52616b"))
    canvas.drawString(50,760,"TÓPICOS DE BIG DATA  |  GRUPO 512")
    canvas.drawString(50,27,"Jorge Adalberto Zuñiga Oliva · JorgeZO")
    canvas.drawRightString(562,27,str(doc.page)); canvas.restoreState()


def pdf_bytes(texto, origen):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer,pagesize=letter,rightMargin=50,leftMargin=50,topMargin=57,bottomMargin=49,
                            author="Jorge Adalberto Zuñiga Oliva",title=texto.splitlines()[0].lstrip("# "))
    doc.build(elementos(texto,origen),onFirstPage=pagina,onLaterPages=pagina)
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--portafolio",type=Path,default=RAIZ/"reportes/Portafolio_JorgeZO.pdf")
    args = parser.parse_args()
    trabajos = [("01_machine_learning.md","Actividad de investigación Machine Learning.pdf"),
                ("02_modelo_predictivo.md","Investigación Modelo predictivo.pdf"),
                ("03_knn.md","KNN (K-Nearest Neighbors) Investigación.pdf"),
                ("04_resumen_regresion.md","Resumen_Modelos_Regresion.pdf"),
                ("05_lectura_esperanza_vida.md","Why is life expectancy in the US lower than in other rich countries.pdf")]
    escritor = PdfWriter()
    portada = "# Portafolio de prácticas e investigaciones\n\n**Jorge Adalberto Zuñiga Oliva**\n\nMatrícula 82005 · Grupo 512 · Tópicos de Big Data\n\n28 de octubre de 2026\n\n## Contenido\n\nCinco investigaciones con referencias y catorce reportes de prácticas ejecutadas.\n\nLos reportes resumen métodos y resultados. El código completo, respuestas y salidas se encuentran en los notebooks del repositorio.\n\n[Repositorio e índice de actividades](https://github.com/JorgeZO/BigData512).\n\nLos marcadores de este PDF permiten navegar a cada documento.\n\nLas extrapolaciones demográficas se presentan como escenarios bajo supuestos, y el archivo de ventas se identifica como recorte de clase."
    escritor.append(BytesIO(pdf_bytes(portada,RAIZ/"README.md")),outline_item="Contenido")
    rutas = [(RAIZ/"investigaciones"/md_nombre, RAIZ/pdf_nombre) for md_nombre,pdf_nombre in trabajos]
    for resumen in sorted((RAIZ/"reportes/resumenes").glob("*.md")):
        rutas.append((resumen,RAIZ/"reportes/pdf"/(resumen.stem.split("__",1)[1]+".pdf")))
    for origen,destino in rutas:
        texto = origen.read_text(encoding="utf-8"); contenido = pdf_bytes(texto,origen)
        destino.parent.mkdir(parents=True,exist_ok=True); destino.write_bytes(contenido)
        escritor.append(BytesIO(contenido),outline_item=texto.splitlines()[0].lstrip("# "))
        print(f"PDF: {destino.relative_to(RAIZ)}",flush=True)
    args.portafolio.parent.mkdir(parents=True,exist_ok=True)
    escritor.add_metadata({"/Title":"Portafolio Big Data - JorgeZO","/Author":"Jorge Adalberto Zuñiga Oliva"})
    escritor.write(args.portafolio)
    print(f"Portafolio: {args.portafolio} ({len(escritor.pages)} páginas)")


if __name__ == "__main__": main()
