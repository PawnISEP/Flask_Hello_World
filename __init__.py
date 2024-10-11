from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    parite = "pair" if (valeur1 + valeur2) % 2 == 0 else "impair"
    return f"<h2>La somme de vos valeurs correspond à : {valeur1 + valeur2}</h2><p>C'est un nombre {parite}.</p>"
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)


