import os
from flask import Flask, render_template, jsonify, request, Response
from flask_request_arg import request_arg
from main import *

app = Flask(__name__)
app.config['SESSION_REFRESH_EACH_REQUEST'] = True # Permet d'effectuer des requêtes de façon simultanées

@app.route("/")
def index():
    """ None -> flask
    Préconditions : Un fichier « index.html » est présent dans le dossier « /templates »
    Rôle: Affiche la page web présent dans le dossier /templates"""
    return render_template('index.html') 

@request_arg('value', str)
@app.route('/submit_form', methods=['GET','POST'])
def submit_form(): 
     """ None -> flask
     Préconditions : Un formulaire a été saisie sur la page web et récupéré dans le programme sous forme d'un str et un fichier « index.html » est présent dans le dossier « /templates »
     Les fonctions readDateCSV et execute doivent également exister.
     Rôle: Récupère les données soumises par le formulaire et exécute l'analyse de données pour la date requise tout en affichant la page web présent dans le dossier /templates à la fin de l'exécution"""
     date = request.args.get('value')
     resultat = readDateCSV(str(date))
     execute(str(date),resultat)
     return render_template('index.html')



