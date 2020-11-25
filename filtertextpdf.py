"""
	Name:
		filtertextpdf

	Descripcion:
		Este modulo permite agregar o editar filtros para extraer mejor la información
		hace uso del modulo re y string.
"""
import re
import string

def customizable1(text):
	def dicPersona(text):
		data = text[6].split("AGE ")[1]
		dnombre = text[5].split()[0]
		dedad = text[5].split()[1]
		dsexo = text[5].split()[2]
		dfecha = (text[5].split(dsexo)[1]).strip()
		nombre = re.findall("^[A-Za-z\\W]{0,}", data)[0]
		resto = data.split(nombre)[1]
		edad = resto.split()[0]
		sexo = resto.split()[1]
		fecha = resto.split()[2]

		dPersonas = {}
		dPersonas[dnombre] = nombre
		dPersonas[dedad] = edad
		dPersonas[dsexo] = sexo
		dPersonas[dfecha] = fecha
		return dPersonas

	def extScore(text):
		aScore = []
		sec_lista = [
			text[8],
			text[11],
			text[13],
			text[15],
			text[17],
			text[19],
			text[21],
			text[24],
			text[28],
			text[30],
			text[32],
			text[34].strip(" |"),
			text[36].strip(" |"),
			text[37].strip(" I")
		]

		def seachScore(string):
			return re.findall("[.0-9]{0,}.[sechzN/Abpm ]{0,3}$", string)
			
		listaSEC = map(seachScore, sec_lista)
		

		i = 0
		for sec in listaSEC:
			aScore.append( sec[0] )
			i += 1

		return aScore

	try:
		diccionario = {}
		diccionario["titulo"] = text[0]
		diccionario["persona"] = dicPersona(text)
		diccionario["subtitle"] = (text[6].split(diccionario["persona"]["NAME"])[0]).strip()
		en = text[7].split()
		diccionario[en[0] + en[1]] = {1: text[8:37]}
		diccionario[en[2]] = extScore(text)
		return diccionario

	except Exception as e:
		print("Error al filtrar el text")
		return False

def customizable2(text):
	diccionario = {}
	i = 0
	for t in text:
		t = t.strip(" ")
		if re.findall("^(Congratulations on completing your)", t) or re.findall("^(your performance. Your estimated Functional)", t) or re.findall("^(important age biomarkers. Your)", t) or re.findall("^(percentile of 50% represents)", t) or re.findall("^(important age biomarkers. Your)", t) or re.findall("^(Important health indicator, but excluded)", t):
			t = ""
		if re.findall("^[-_?<>|~*:@)]", t) or re.findall("[-_?<>|~*:@)]$", t):
			t = t.replace("\"", "")
			t = t.replace("-", "")
			t = t.replace("_", "")
			t = t.replace("~", "")
			t = t.replace("/", "")
			t = t.replace(">", "")
			t = t.replace("<", "")
			t = t.replace("*", "")
			t = t.replace("@", "")
			t = t.replace("?", "")
			t = t.replace("|", "")
			t = t.replace(":", "")
		
		if t != "":
			diccionario[i] = t
			i += 1
	return diccionario

def customizable3(text):
	diccionario = {}
	i = 0
	for t in text:
		diccionario[i] = t
		i += 1
	return diccionario
