from flask import Flask, jsonify, request
import json
# Importar el modulo necesario para convert PDF a texto
import _pdftotext

app = Flask(__name__)

# Get Data Routes

@app.route('/convert_pdf', methods=['GET'])
def convert_pdf():        
	def voidP(name):
		if request.args.get(name) != None:
			return request.args.get(name)
		else:
			return ""
	
	pdf = voidP("file")
	
	if pdf == "":
		return "No se ha adjunta un archivo PDF"
	else:

		file = _pdftotext.extract(pdf, json=voidP("json"), typeFilter=voidP("typeFilter"))
		return jsonify(json=file)


if __name__ == '__main__':
	app.run(debug=True, port=4000)
