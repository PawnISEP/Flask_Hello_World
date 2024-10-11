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

@app.route('/somme/<path:valeurs>')
def somme(valeurs):
    valeurs_list = list(map(int, valeurs.split('/')))
    total = 0

    for i in valeurs_list:
      total = total + i
  
    parite = "pair" if (total) % 2 == 0 else "impair"
    return f"<h2>La somme de vos valeurs correspond à : {total}</h2><p>C'est un nombre {parite}.</p>"

@app.route('/max/<path:valeurs>')
def max_value(valeurs):
    valeurs_list = list(map(int, valeurs.split('/')))
    valeur_max = valeurs_list[0]
    
    for valeur in valeurs_list:
        if valeur > valeur_max:
            valeur_max = valeur
    return f"<h2>La valeur la plus importante parmi {valeurs_list} est : {valeur_max}</h2>"

                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)


