from librairie import Librairie
from flask import Flask, jsonify, request

app = Flask(__name__)

librairie1 = Librairie("La petite Libraire", "199 Rue de la boustifaille", ["Harry Potter", "Le Python pour les nuls"])

print(librairie1.get_nom())
print(librairie1.get_addresse())
print(librairie1.get_livres())

librairie1.add_livres("DevOps")

print(librairie1.get_livres())

librairie1.del_livres("DevOps")

print(librairie1.get_livres())

@app.route("/nom")
def getnom():
    return jsonify(librairie1.get_nom())

@app.route("/livres")
def getlivres():
    return jsonify(librairie1.get_livres())

@app.route('/livres', methods=['POST'])
def addlivres():
    livre = request.get_json()
    print(livre)
    librairie1.add_livres(livre['nomLivre'])
    return "", 204

@app.route('/livres', methods=['DELETE'])
def dellivres():
    livre = request.get_json()
    print(livre)
    librairie1.del_livres(livre['nomLivre'])
    return "", 204