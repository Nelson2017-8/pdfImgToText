"""
	Name:
		pdftotext

	Descriptcion:
		Este modulo permite convertir un PDF a Text y exportarlo a JSON, hace uso 
		de un lector ORC y además importa funcionalidades de otros modulos

"""
import os
import exportpdf
import image
import time
import extractiontext
import filtertextpdf


def extract(file, filterChars="", filterImg="", fileJsonSave=""):
	"""
		Funcion extract:
			Recibe 4 parametros, el primer parametros es el nombre y ubicacion del PDF y los otros
			3 son opcionales, nos permite agregar funcionalidad al programa:
				* Parametro "filterChars": Permite filtrar caracteres como @ o |. Por defecto esta habilitada
				* Parametro "filterImg": Nos permite aplicar un filtro a las images que se extraigan de un PDF tenga en cuenta que este proceso puede hacer que el programa tarde más, pero no facilita la lectura ORC de modo que el texto sea más preciso
				* Parametro "fileJsonSave": Nos permite especificar el nombre y ubicación del archivo JSON al cual se guardaran los datos extraidos del PDF

			Nota: Estos paramatros son introduccidos por URL mediante GET.

			Ejemplo de Uso:
				* Desactivar Filtro de Caracteres:
					http://dominio.com/NOMBRE_PDF.pdf?filterChars=False

				* Activar el filtro de imagen:
					http://dominio.com/NOMBRE_PDF.pdf?filterImg=True

				* Agregar nombre del archivo JSON personalizado
					http://dominio.com/NOMBRE_PDF.pdf?fileJsonSave=PDF.json
	"""
	if filterChars == "":
		filterChars = True
    
	if filterImg == "":
		filterImg = False

	if fileJsonSave == "":

		fileJsonSave = "data.json"

	print("File: " + file)
	print("filterChars: " + str(filterChars))
	print("filterImg: " + str(filterImg))
	print("fileJsonSave: " + str(fileJsonSave))

	images = exportpdf.convert(file, os.path.splitext(file)[0] + '/')
	# Si images devuelve una tupla signica que logro extraer las images con exito
	if images != False:
		print("Se han extraido las imagenes del PDF")
		# Si el archivo tiene más de una pagina, creara más imagenes dentro de la tupla
		for img in images:
			# Aplicar filtro de imagen. Por defecto esta desactivado
			# El filtro ayuda a mejorar la imagen para mejor lectura del texto
			# pero es más pesado y tarda más
			
			if filterImg == True:
				print("Aplicando filtros a las images, esto mejora mucho la calidad pero el proceso tarda más")			
				image_filter = image.filter(img)
			else:
				# Si el filtro esta desactivo solo le asginamos el valor de la img
				# que es extraido de la tupla images donde contiene las ubicaciones
				# de las imagenes
				image_filter = img

			# Verificamos que no tengamos ningun error
			if image_filter != False:
				# Convertimos las images a texto, sino se logra convertir genera False
				texto = image.convertText(image_filter)
				if texto != False:
					print("Se ha generado el texto")
					
					text = extractiontext.init(None)
					diccionario = filtertextpdf.customizable2(text)
					diccionario2 = filtertextpdf.customizable3(text)

					if filterChars == True:
						if isinstance(diccionario,dict):
							fileJson = extractiontext.ejson(diccionario, fileJsonSave)
							if fileJson != False:
								print("Se ha generado un JSON")
								return fileJson
							else:
								return "Ah ocurrido un error"
					else:
						if isinstance(diccionario2, dict):
							fileJson = extractiontext.ejson(diccionario, fileJsonSave)
							if fileJson != False:
								print("Se ha generado un JSON")
								return fileJson
							else:
								return "Ah ocurrido un error"
							print("Se ha generado un JSON2")
				else:
					print("No se ha podido extraer el texto")
			else:
				print("No se ha podido aplicar filtro a la imagen")
	else:
		print("No se ha podido convertir la imagen")
