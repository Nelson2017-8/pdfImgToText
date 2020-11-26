"""
	Name:
		_filters

	Descripcion:
		Este modulo permite agregar o editar filtros para extraer mejor la información
	
	Requisitos:
		* pillow
		* pytesseract
		* open-cv
"""
import json, _image, pytesseract, string, re, cv2, os
from PIL import ImageEnhance, ImageFilter
from PIL import Image


def exportJSON(diccionario, jsonout):
	"""
		Función esportJSON	
			Descripción:
				La función exportJSON permite generar un archivo JSON, verifica si el diccionario pasado es valido, en caso contario devuelve False.
			
			Parametros:
				* diccionario: El diccionario de python con los datos
				* jsonout: Nombre del fichero JSON a guardar
	"""
	if isinstance(diccionario, dict):
		with open(jsonout, 'w') as file:
		    json.dump(diccionario, file, indent=4)
		print("Operación finalizada")
		return diccionario
	else:
		print("Operación no finalizada")
		return False

def option1(img, outputDir, jsonout = "", option2 = False):
	"""
		Filtro option1:
		
			Descripción:
				Filtro 1 y 2, este recorta la imagen en 10 partes y las leer por separando, solo es válido para PDF del mismo patrón o la misma estructura.

			Parametros:
				* img: Imagen
				* outputDir: Directorio donde se guardaran los recortes de la imagen, si no existe la carpeta lo crea.
				* option2: Habilita el filtro numero 2
	"""
	if jsonout == "":
		jsonout = "exportJSON.json"

	# Creamos la carpeta de recortes
	if not os.path.exists(outputDir):
		os.makedirs(outputDir)
	try:

		aImage = [
			outputDir+"title.jpg",
			outputDir+"number.jpg",
			outputDir+"subTitle.jpg",
			outputDir+"name.jpg",
			outputDir+"age.jpg",
			outputDir+"gender.jpg",
			outputDir+"textDate.jpg",
			outputDir+"biomarkerTest.jpg",
			outputDir+"score.jpg",
			outputDir+"percentile.jpg"
		]

		# Hago varios recortes de la imagen
		print("Recortando Imagenes...")


		_image.cropfile(img, aImage[0], 0, 7500, 0, 750)
		_image.cropfile(img, aImage[1], 311, 4128, 1316, 658)
		_image.cropfile(img, aImage[2], 979, 3460, 1316, 658)
		_image.cropfile(img, aImage[3], 4687, 1070, 1459, 399)
		_image.cropfile(img, aImage[4], 5757, 243, 1459, 399)
		_image.cropfile(img, aImage[5], 6000, 441, 1459, 399)
		_image.cropfile(img, aImage[6], 6441, 529, 1459, 399)
		_image.cropfile(img, aImage[7], 311, 2078, 2138, 6228)

		if option2 == True:
			_image.filter(img)

		_image.cropfile(img, aImage[8], 2389, 1131, 2138, 6228)
		_image.cropfile(img, aImage[9], 3520, 3720, 2138, 6228)

		print("Aplicando Filtros...")
		# Aplica filtros blanco y negro a las imagenes
		for file in aImage:
			_image.filter(file)

		# Creo un diccionario para almacenar los datos extraidos
		print("Leyendo archivos...")
		diccionario = {}

		# TITULO
		titulo = pytesseract.image_to_string(Image.open(aImage[0]))
		titulo = titulo.strip()

		if not re.findall("^[A-Z]", titulo):
			# filtra si hay caracteres iniciales antes del titulo
			titulo = re.findall("[A-Z].*$", titulo)[0]

		diccionario["title"] = titulo

		# Numero
		num = pytesseract.image_to_string(Image.open(aImage[1]))
		num = num.strip()
		num = num.replace(" ", "")
		num = re.findall("([0-9]{0,})", num)[0]
		diccionario["number"] = num

		# Subtitulo
		subt = pytesseract.image_to_string(Image.open(aImage[2]))
		subt = subt.strip()
		diccionario["subtitle"] = subt

		## Diccionario Personas
		person = {}
		# Name
		name = pytesseract.image_to_string(Image.open(aImage[3]))
		name = name.strip()
		tname, name = name.split("\n")
		person[tname] = name

		# age
		age = pytesseract.image_to_string(Image.open(aImage[4]))
		age = age.strip()
		tage, age = age.split("\n")
		person[tage] = age

		# gender
		gender = pytesseract.image_to_string(Image.open(aImage[5]))
		gender = gender.strip()
		tgender, gender = gender.split("\n")
		person[tgender] = gender

		# dateTest
		dateTest = pytesseract.image_to_string(Image.open(aImage[6]))
		dateTest = dateTest.strip()
		dateTest = dateTest.strip("|")
		dateTest = dateTest.strip()
		tdateTest, dateTest = dateTest.split("\n")
		person[tdateTest] = dateTest

		diccionario["person"] = person

		# Biomarker test
		bio = pytesseract.image_to_string(Image.open(aImage[7]))
		bio = bio.strip()
		tBio = bio.split("\n")[0]
		cBio = bio.replace(bio.split("\n")[0], "").strip()
		diccionario[tBio] = cBio

		# SCORE
		Score = pytesseract.image_to_string(Image.open(aImage[8]))
		Score = Score.strip()
		tScore = Score.split("\n")[0]
		cScore = Score.replace(Score.split("\n")[0], "").strip()
		diccionario[tScore] = cScore

		# PERCENTILE
		Porcentile = pytesseract.image_to_string(Image.open(aImage[9]))
		# print(Porcentile)
		Porcentile = Porcentile.strip()
		tPorcentile = Porcentile.split("\n")[0]
		cPorcentile = Porcentile.replace(Porcentile.split("\n")[0], "").strip()
		diccionario[tPorcentile] = cPorcentile

		print("Creando archivo JSON...")
		# print(diccionario)
		return exportJSON(diccionario, jsonout)

	except Exception as e:
		print("Ha ocurrido un error")
		print(e)
		return "Ha ocurrido un error al filtrar los datos"

# img = "AgeMeter-PDF document-9956D3F25BA8-1 2/img1.jpg"
# path = "AgeMeter-PDF document-9956D3F25BA8-1 2/recortes/"

# option1(img, path, "exportJSON.json")

def option3(img, jsonout):
	"""
		filtro option3
			Descripción:
				Filtro universal para casí cualquier PDF

			Parametros:
				* img: Imagen
				* outputDir: Directorio donde se guardaran los recortes de la imagen, si no existe la carpeta lo crea
	"""
	if jsonout == "":
		jsonout = "exportJSON.json"

	print("Aplicando Filtro...")
	_image.filter(img)
	print("Leyendo archivos...")
	text = pytesseract.image_to_string(Image.open(img))
	text = text.strip()
	text = text.split("\n")
	diccionario = {}
	i = 0
	for t in text:
		if t != "" and t != " ":
			diccionario[i] = t
			i += 1
	# print(diccionario)
	return exportJSON(diccionario, jsonout)

# option3(img, "exportJSON.json")
