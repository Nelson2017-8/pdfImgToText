"""
	Nonmbre:
		image

	Descripción:
		Este modulo permite manipulas las images para detectar texto
		mediante un Lector de ORC o aplicar un filtro para mejorar
		la calidad a la hora de detectar texto en una imagen

	Requerimientos:
		* pillow: Requiere tener pillow instalado puede instalarlo mediante pip
		* pytesseract: Puede ser instalado desde pip
		* tesseract: El lector ORC su instalación varia dependiendo el Sistema operativo
		  para más información consulte la documentación
"""

from PIL import ImageEnhance, ImageFilter
from PIL import Image
import os
import pytesseract
from io import open


def filter(file):
	"""
		Función filter:
			Permite aplicar un filtro de alto contraste para mejorar
			la lectura del texto mediante ORC. La funcion recibe como
			parametro la ubicación de la imagen, devuelve False en caso
			de error o devuelve la ubicación de la nueva imagen
	"""
	try:
		im = Image.open(file)
		im = im.filter(ImageFilter.MedianFilter())
		enhancer = ImageEnhance.Contrast(im)
		im = enhancer.enhance(15)
		im = im.convert('1')
		outputFile = os.path.splitext(file)[0] + ".jpg"
		im.save(outputFile)
	except Exception as e:
		print(e)
		return False

	return outputFile


"""
	pytesseract.pytesseract.tesseract_cmd = r'UBICACIÓN DEL tesseract'
	Esta linea de codigo necesario si se trabaje en windows y no se ha agregado
	el tesseract al PATH o variable globales, para más información consulte la
	documentación
"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def convertText(file, generatText = True, txt = "_image.txt"):
	"""
		Función convertText:
			Permite reconocer texto en una imagen mediante un lector ORC.
			Recibe dos parametro el primero es la imagen, el segundo es
			un valor de verdadero/falso (por defecto es True) que nos permite
			guardar el texto en un archivo de texto. El ultimo parametro es
			un la ubicación y nombre del archivo de texto donde se guardara el texto 
			reconocido, si en el segundo parametro se coloco True no se genera
			un archivo de texto
	"""

	try:
		text = pytesseract.image_to_string(Image.open(file))

	except Exception:
		print(e)
		print("No se pudo extraer el texto de la imagen")
		return False
	
	if generatText == True:
		try:
			archivo_text = open(txt, "w")
			archivo_text.write(text)

		except Exception:
			print("No se pudo generar un Texto de la imagen: " + str(file) )
	return True
