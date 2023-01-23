from tabulate import tabulate
from fpdf import FPDF
import pdfrw
from graphs import *
from visualisation import *
import os

def reportDF(resultat):
    """ DataFrame -> None
    Préconditions : la fonction CreateDataframe doit exister
    Rôle : Crée et enregistre le DataFrame passé en paramètre vers un fichier .pdf"""
    df = CreateDataframe(resultat)
    table = tabulate(df, headers='keys', tablefmt='pretty', showindex=True)
    
    # Initialiser un objet FPDF pour créer le PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=9)

    # Ajouter chaque ligne de la table au PDF
    for row in table.split('\n'):
        pdf.cell(40, 10, row, 0, 1)

    # Enregistrer le PDF
    output_path = os.path.join("static","dataframe-report.pdf")
    pdf.output(output_path)
    return

def reportDescribeDF(resultat):
    """ DataFrame -> None
    Préconditions : la fonction CreateDataframe doit exister
    Rôle : Crée et enregistre le DataFrame passé en paramètre et détaillée vers un fichier .pdf"""
    data = CreateDataframe(resultat)
    df = CreateDescribeData(data)
    table = tabulate(df, headers='keys', tablefmt='pretty', showindex=True)
    
    # Initialiser un objet FPDF pour créer le PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=8)

    # Ajouter chaque ligne de la table au PDF
    for row in table.split('\n'):
        pdf.cell(40, 10, row, 0, 1)
    output_path = os.path.join("static","datadesc-report.pdf")
    # Enregistrer le PDF
    pdf.output(output_path)
    return

def mergePDF(resultat):
    """ DataFrame -> None
    Préconditions : les fonctions reportDF et reportDescribeDF et les fichiers "data-graph.pdf","dataframe-report.pdf","datadesc-report.pdf" doivent exister
    Rôle: Fusionne les pdf de chaque rapport entre eux"""
    #Appel les précédentes fonctions pour créer les fichiers .pdf
    reportDF(resultat)
    reportDescribeDF(resultat)
    
    #Création des liens vers fichiers .pdf
    output = pdfrw.PdfWriter()
    
    input_path1 = os.path.join("static", "data-graph.pdf")
    input_path2 = os.path.join("static", "dataframe-report.pdf")
    input_path3 = os.path.join("static", "datadesc-report.pdf")
    output_path = os.path.join("static","data-report.pdf")
    
    #Fusion des pages .pdf
    input1 = pdfrw.PdfReader(input_path1)
    input2 = pdfrw.PdfReader(input_path2)
    input3 = pdfrw.PdfReader(input_path3)
    output.addpages(input1.pages)
    output.addpages(input2.pages)
    output.addpages(input3.pages)
    output.write(output_path)
    return

def execute(date,resultat):
    """ str,DataFrame -> None
    Préconditions : les fonctions tracerGraphique et mergePDF doivent exister
    Rôle: Trace le graphique et génère le rapport .pdf du DataFrame"""
    tracerGraphique(date,resultat)
    mergePDF(resultat)
    return