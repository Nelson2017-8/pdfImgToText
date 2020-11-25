from flask import Flask, jsonify, request
import json
# Importar el modulo necesario para convert PDF a texto
import pdftotext

app = Flask(__name__)

# Get Data Routes
@app.route('/pdf/<string:nombrePDF>', methods=['GET', 'POST'])
def pdf(nombrePDF):        
    def voidP(name):
        if request.args.get(name) != None:
            return request.args.get(name)
        else:
            return ""

    file = pdftotext.extract(nombrePDF, filterChars=voidP("filterChars"), filterImg=voidP("filterImg"), fileJsonSave=voidP("fileJsonSave"))
    return jsonify(json=file)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
