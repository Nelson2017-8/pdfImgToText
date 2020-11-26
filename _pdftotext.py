"""
	Name:
		_pdftotext

	Descripción:
		Este modulo permite convertir un PDF a Texto y exportarlo a JSON, hace uso de un lector OCR y además importa funcionalidades de otros modulos, para opciones personalizadas de filtros modifique el modulo _filters

"""
import time, os, _exportpdf, _image, _filters
from shutil import rmtree


def extract(file, json="", typeFilter=""):
	"""
		Funcion extract:
			Descripción:
				Extraer la información de un archivo PDF, nos permite seleccionar entre varios filtros y permite guardar la información en un archivo JSON
				
			Parametros:
				* file: Nombre o URL del archivo PDF
				* json: Nos permite especificar el nombre del archivo JSON donde se guardaran los datos extraidos del PDF
				* typeFilter: El tipo de filtro seleccionado, actualmente tiene 3 tipos de filtros. El primero y segundo nos permiten recortar la imagen y sacar los datos por separados, esta funcionalidad solo es válida para los PDF con una estructura similar. El tercer filtro es más universal permite estraer todo el texto linea por linea, es aplicable a la mayoría de los PDF.

			Nota: Estos paramatros son introducidos y recibidos por GET.

			Ejemplo de Uso:
				* Modo básico: Por defecto el programa usa el tipo de filtro 1 y guarda los datos con el nombre de data.json
					http://dominio.com?file=NOMBRE_PDF.pdf

				* Cambiar nombre al archivo JSON:
					http://dominio.com?file=NOMBRE_PDF.pdf&json=export.json

				* Cambiar el tipo de filtro aplicado:
					http://dominio.com?file=NOMBRE_PDF.pdf&typeFilter=2
	"""
	if typeFilter == "":
		typeFilter = "1"

	if json == "":
		json = "data.json"

	print("File: " + file)
	print("json: " + str(json))
	print("typeFilter: " + str(typeFilter))

	namePDF = os.path.splitext(file)[0]
	images = _exportpdf.convert(file, namePDF + '/')
	# Si images devuelve una tupla significa que logro extraer las images con exito
	if images != False:
		print("Se han extraido las imagenes del PDF")
		# Si el archivo tiene más de una pagina, creara más imagenes dentro de la tupla
		res = []
		for img in images:

			# Opciones de Filtro de texto
			if typeFilter == "1":
				# Filtro 1
				res.append(_filters.option1(img, namePDF + '/recortes/', json))
			elif typeFilter == "2":
				# Filtro 2
				res.append(_filters.option1(img, namePDF + '/recortes/', json, True))
			elif typeFilter == "3":
				# Filtro 3
				res.append(_filters.option3(img, json))
			else:
				return "Error: El tipo de filtro seleccionado no ha sido encontrado"

		# Eliminar la carpeta de imagenes
		rmtree(namePDF + '/')
		return res
	else:
		print("No se ha podido convertir la imagen")
		return "Error: No se puedo extraer las imagenes del PDF"
