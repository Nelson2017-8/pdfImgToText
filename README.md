# Programa de conversión de PDF a Texto
***

## Descripción
Este programa permite Convertir un PDF a Imagen para luego extraer el texto y ser exportado y visualizado en un archivo JSON, este programa hace uso del Framework de Python Flask. Además el programa hace uso de filtros personalizados, existen 3 filtros básicos.

## Requisitos
Para poder usar este programa adecuadamente debe tener instalador las siguientes librerías y dependecias:

	1 Flask
	2 Pillow
	3 Pytesseract 
	4 Tesseract
	5 pdf2image
	6 open-cv (Python)

## Instalando dependecias

### Flask

pip install flask

### Pillow

pip install pillow

### Pytesseract

pip install pytesseract

### Tesseract

Este normalemente viene con algunas distribuciones de Linux, en caso contrario de no tenerlo instalado se puede instalar con:

	apt update
	apt upgrade
	apt install tesseract-ocr

### pdf2image

Normalemente viene con algunas distribuciones de Linux, en caso contrario de no tenerlo instalado se puede instalar con :

pip install pdf2image 

### open-cv (Python)
pip install opencv-python


## Uso:
Para usar el programa debe tener todas las depencias instaladas y configuradas, si es asi nos basta con ir a app.py Corremos el programa y desde el navegador nos vamos a http://dominio.com/NOMBRE_PDF.pdf

Ejemplo de Uso:
* Modo básico: Por defecto el programa usa el tipo de filtro 1 y guarda los datos con el nombre de data.json
	http://dominio.com?file=NOMBRE_PDF.pdf

* Cambiar nombre al archivo JSON:
	http://dominio.com?file=NOMBRE_PDF.pdf&json=export.json

* Cambiar el tipo de filtro aplicado:
	http://dominio.com?file=NOMBRE_PDF.pdf&typeFilter=2

### Filtros:

Existen 3 tipos de filtros:

	* Filtro 1: Aplicable solo a la estructura del PDF (AgeMeter-PDF document-9956D3F25BA8-1 2.pdf), este recorta el PDF en 10 imagenes donde extrae la información por separada aplicando filtros a blanco y negro

	* Filtro 2: Igual que el filtro 1 este tambien recorta el PDF en 10 partes a diferencia que mejora el filtro para tener mejor calidad

	* Filtro 3: Este filtro es universal, es aplicacble a casi cualquier PDF. A diferencia de los anteriores este no extrae los datos denpendiendo del tamaño y estructura del PDF
