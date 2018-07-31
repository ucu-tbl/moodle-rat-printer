import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# LISTA DE PREGUNTAS
# Estructura donde se guardaran las preguntas /
    # gridQuiz[x][] # numero pregunta
    # gridQuiz[][0] # Titulo
    # gridQuiz[][1] # Pregunta
    # gridQuiz[][2] # Tipo de Pregunta
    # gridQuiz[][3] # Imagen
    # gridQuiz[][4] # Cantidad de Respuestas
    # gridQuiz[][5] # Respuesta 1
    # gridQuiz[][6] # Respuesta 2
    # gridQuiz[][7] # Respuesta 3 ...
 
def convertir(listaPreguntas):
    nombrePrueba = "PROGFUN-RAT1 Lenguaje funcional básico"
    nombreArchivo = nombrePrueba +".pdf"

    documento = SimpleDocTemplate(nombreArchivo,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
    Prueba=[]
    
    #logo = "python_logo.png"
    #magName = "Pythonista"
    #issueNum = 12
    #subPrice = "99.00"
    #limitedDate = "03/05/2010"
    #freeGift = "tin foil hat"
 
    diaHora = time.ctime()
    #full_name = "Magela Carballo"
    #address_parts = ["411 State St.", "Marshalltown, IA 50158"]
 
    #im = Image(logo, 2*inch, 2*inch)
    #Prueba.append(im)
 
    # DIA Y HORA
    estiloFecha=getSampleStyleSheet()
    estiloFecha.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    lineaFecha = '<font size=12>%s</font>' % diaHora
    Prueba.append(Paragraph(lineaFecha, estiloFecha["Normal"]))
    Prueba.append(Spacer(1, 12))
 
    # NOMBRE DE LA PRUEBA
    estiloTitulo=getSampleStyleSheet()
    estiloTitulo.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    lineaTitulo = '<font size=13>%s</font>' % nombrePrueba
    Prueba.append(Paragraph(lineaTitulo, estiloTitulo["Normal"]))  
    Prueba.append(Spacer(1, 12))

    # Preguntas y Respuestas
    estiloTituloPregunta=getSampleStyleSheet()
    estiloTituloPregunta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    estiloPregunta=getSampleStyleSheet()
    estiloPregunta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    estiloRespuesta=getSampleStyleSheet()
    estiloRespuesta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    estiloNumPregunta=getSampleStyleSheet()
    estiloNumPregunta.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    numPreg = 1

    for pregunta in listaPreguntas:

    #    gridQuiz[0][0]= titulo
    #    gridQuiz[0][1]= pregunta
    #    gridQuiz[0][2] = tipopregunta
    #    gridQuiz[0][3] = imagen
    #    gridQuiz[0][4] = cantidad de respuestas
    #    gridQuiz[0][4] = cantidad de respuestas

        # Numero Pregunta
        lineaNumeroPregunta = '<font size=9>Pregunta %s</font>' % numPreg
        Prueba.append(Paragraph(lineaNumeroPregunta, estiloNumPregunta["Normal"])) 

        #Titulo de la Pregunta - Opcional
        lineaTituloPregunta = '<font size=12>%s</font>' % pregunta[0]
        Prueba.append(Paragraph(lineaTituloPregunta, estiloTituloPregunta["Normal"])) 

        #Texto de la Pregunta
        lineaPregunta = '<font size=12>%s</font>' % pregunta[1]
        Prueba.append(Paragraph(lineaPregunta, estiloPregunta["Normal"])) 

        # Respuestas
        for i in range(5,5+pregunta[4]):
            lineaRespuesta = '<font size=12>%s</font>' % pregunta[i]
            Prueba.append(Paragraph(lineaRespuesta, estiloRespuesta["Normal"]))
        Prueba.append(Spacer(1, 12))

        numPreg = numPreg + 1         

    documento.build(Prueba)