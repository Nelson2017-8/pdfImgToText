from io import open
import json

def init(txtFlat = None, textFile = "_image.txt"):
	
	if txtFlat == None:
		# Si no pasamos un variable de texto intenta leer un archivo de text
		try:
			file = open(textFile, "r")
			text = []
			while(True):
			    linea = file.readline()

			    if (linea != "") and (linea != "\n") and (len(linea) > 3):
				    # print(linea)
				    text.append(linea.strip())
			    if not linea:
			        break

			file.close()
			del(file)
			return text

		except Exception as e:
			print("Error No se puedo abrir o procesar el archivo de texto: " + textFile)
			return False

def ejson(diccionario, nameJson):
	#importar a JSON
	with open(nameJson, 'w') as file:
		json.dump(diccionario, file, indent=4)
	
	return diccionario