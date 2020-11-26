"""
	Nonmbre:
		_image

	Descripción:
		Este modulo permite manipular las images para reconocer texto mediante un Lector de OCR o aplicar un filtro para mejorar la calidad

	Requerimientos:
		* pillow
		* pytesseract
		* tesseract
"""

from PIL import ImageEnhance, ImageFilter
from PIL import Image
import os
import pytesseract
from io import open
import cv2

def filter(file):
	"""
		Función filter:
			Permite aplicar un filtro de alto contraste para mejorar la lectura de texto mediante OCR. La funcion recibe como parametro la ubicación de la imagen, devuelve False en caso de error o devuelve la ubicación de la nueva imagen
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
	
	Esta linea de codigo necesario si se trabaje en windows y no se ha agregado el tesseract al PATH o variable globales
"""
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
def convertText(file, txt = "_image.txt"):
	"""
		Función convertText:
			Descripción:
				Permite reconocer texto en una imagen mediante un lector OCR y guardarlo en un archivo de texto

			Parametros:
				* file: archivo de Imagen
				* txt: nombre del archivo de texto donde se guardaran los datos
	"""

	try:
		text = pytesseract.image_to_string(Image.open(file))

	except Exception:
		print(e)
		print("No se pudo extraer el texto de la imagen")
		return False
	
	archivo_text = open(txt, "w")
	archivo_text.write(text)

	return True

def cropfile(pathin, pathout, x, w, y, h):
	"""
		Funcion cropfile:
			Descripción: 
				Esta funcion recorta una imagen y la guarda con un nombre diferente. 
			
			Parametros:
				* pathin: Imagen a recortar
				* pathout: Nombre final del recote
				* x: Dimensión en x de la imagen
				* y: Dimensión en y de la imagen
				* w: Ancho de la imagen
				* h: Alto de la imagen
	"""
	img = cv2.imread(pathin)
	crop_img = img[y:y+h, x:x+w]
	cv2.imwrite(pathout, crop_img)
	return True