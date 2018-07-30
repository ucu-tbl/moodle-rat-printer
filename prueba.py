import tkinter.filedialog as fd
from tkinter import filedialog
from tkinter import *
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from tkinter import *
import time


def salirPDF():
 #	archivo=fd.askdirectory()	
 	archivo="nombrearchivo.pdf"
 	imprimirPDF(archivo)

def imprimirPDF(archivo):
	doc = SimpleDocTemplate(archivo, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
	Story = []
	#logotipo = "/home/decodigo/Documentos/python/python_logo.png"
	nombreRevista = "Programación Avanzada"
	numero = 4
	precio = "10.00"
	fechaLimite = "27/09/2017"
	obsequio = "Taller de Python"
	formatoFecha = time.ctime()
	nombreCompleto = "José Rodriguez"
	partesDeDireccion = ["Calle con número 123", "Colonia, Código Postal 12345"]
	#imagen = Image(logotipo, 1 * inch, 1 * inch)
	#Story.append(imagen)
	estilos = getSampleStyleSheet()
	estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	texto = '%s' % formatoFecha
	Story.append(Paragraph(texto, estilos["Normal"]))
	Story.append(Spacer(1, 12))
	# Se construye la dirección
	texto = '%s' % nombreCompleto
	Story.append(Paragraph(texto, estilos["Normal"]))
	for part in partesDeDireccion:
  		texto = '%s' % part.strip()
  		Story.append(Paragraph(texto, estilos["Normal"]))
	Story.append(Spacer(1, 12))
	texto = 'Estimado %s:' % nombreCompleto.split()[0].strip()
	Story.append(Paragraph(texto, estilos["Normal"]))
	Story.append(Spacer(1, 12))
	texto = 'Nos gustaría darle la bienvenida como suscriptor a nuestra revista %s ! \
        Recibirá %s números con un precio introductorio de $%s. Por favor responda antes de \
        %s para comenzar a recibir su suscripción y obtenga además su obsequio: %s.' % (nombreRevista,
                                                                                        numero,
                                                                                        precio,
                                                                                        fechaLimite,
                                                                                        obsequio)
	Story.append(Paragraph(texto, estilos["Justify"]))
	Story.append(Spacer(1, 12))
	texto = 'Gracias y esperamos haberle servido.'
	Story.append(Paragraph(texto, estilos["Justify"]))
	Story.append(Spacer(1, 12))
	texto = 'Sinceramente,'
	Story.append(Paragraph(texto, estilos["Normal"]))
	Story.append(Spacer(1, 48))
	texto = 'Daniel López'
	Story.append(Paragraph(texto, estilos["Normal"]))
	Story.append(Spacer(1, 12))
	doc.build(Story)

ventana=Tk()
ventana.title("TBL Printer")
ventana.config(bg="#0B0B61")
ventana.geometry("300x400")
botonAbrir=Button(ventana,text="Seleccionar archivo", command=salirPDF)
botonAbrir.grid(padx=100,pady=100)
ventana.mainloop()


