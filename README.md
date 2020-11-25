# Programa de conversión de PDF a Texto
***

## Descripción
***
Este programa permite Convertir un PDF a Imagen para luego extraer el texto y ser exportado y visualizado en un archivo JSON, este programa hace uso del Framework de Python Flask.

## Requisitos
***
Para poder usar este programa adecuadamente debe tener instalador las siguientes librerías y dependecias:
1 Flask
2 Pillow
3 Pytesseract 
4 Tesseract
5 pdf2image

## Instalando dependecias
***
### Flask
Este es un framework de python puede ser instalado desde PIP con pip install flask

### Pillow
Si no tiene Pillow puede ser instalado desde pip con pip install pillow

### Pytesseract
Esta libreria de python esta disponible en pip se puede instalar con pip install pytesseract

### Tesseract
Este normalemente viene con algunas distribuciones de Linux, en caso contrario de no tenerlo instalado se puede instalar con:
apt update
apt upgrade
apt install tesseract-ocr

### pdf2image
Normalemente viene con algunas distribuciones de Linux, en caso contrario de no tenerlo instalado se puede instalar con pip install pdf2image 

## Uso:
***
Para usar el programa debe tener todas las depencias instladas y configuradas, si es asi nos basta con ir a app.py Corremos el programa y desde el navegador nos vamos a http://dominio.com/NOMBRE_PDF.pdf

Ejemplo de Uso:
1 Desactivar Filtro de Caracteres:
	http://dominio.com/NOMBRE_PDF.pdf?filterChars=False

2 Activar el filtro de imagen:
	http://dominio.com/NOMBRE_PDF.pdf?filterImg=True

3 Agregar nombre del archivo JSON personalizado
	http://dominio.com/NOMBRE_PDF.pdf?fileJsonSave=PDF.json