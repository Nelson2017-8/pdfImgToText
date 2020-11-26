"""
    Nombre:
        _exportpdf
    
    Descripción:
        Este modulo permite convertir PDF a imagenes. Devuelve una lista completa con la ubicación de las imagenes, si un archivo PDF tiene más de una pagina este creara varias imagenes en base al número de paginas. 

    Requerimientos:
        * Tener instalado pdf2image
"""
from pdf2image import convert_from_path
import os


def convert(file, outputDir):
    """ 
        Funcion convert:
            La funcion convert requiere de dos parametros el archivo en formato pdf y la carpeta donde guardara las images, devuel una tupla de las images exportadas o devuelve False en caso de error
            
            Ejemplo de uso:
                convert(pdf, ubicacion_images)

                Para llamarlo sería:
                    exportpdf.convert(pdf, ubicacion_images)

    """
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, 500)
    counter = 1
    imagenes = []
    for page in pages:
        myfile = outputDir +'img' + str(counter) +'.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")
        imagenes.append(myfile)
    else:
        False
    return imagenes
