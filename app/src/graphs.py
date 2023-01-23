import matplotlib.pyplot as plt # Création de graphique et visualisation de données
import numpy as np # Complément visualisation de données
from visualisation import *
import os

def indice_mark(dataframe,donnees,name_indices):
    """ DataFrame,numpy,str-> None
    Préconditions : -
    Rôle: Marque les seuils de dépassement sur le graphique (plot)"""
    DonneesPolluantVitry = dataframe
    seuil_depassee = False
    for i in donnees:
        if not(seuil_depassee):
            plt.annotate("Attention : Seuil "+str(name_indices)+" limite dépassé", xy=(i, DonneesPolluantVitry[name_indices][i]),xytext=(i + 0.9, DonneesPolluantVitry[name_indices][i] - 5), arrowprops=dict(facecolor='red', shrink=0.10),fontsize=12, color='white',bbox=dict(facecolor='red', alpha=0.5))
        seuil_depassee=True
    return
                
def tracerGraphique(date,resultat):
    """ DataFrame -> None
    Préconditions : la fonction CreateDataframe doit exister
    Rôle: Trace le graphique correspondant à la mesure de chaque polluants à Vitry-sur-Seine"""
    DonneesPolluantVitry = CreateDataframe(resultat)
    
    # Attribution des courbes, légendes et titre du graphique linéaire
    plt.plot(DonneesPolluantVitry["NO"],'-*')
    plt.plot(DonneesPolluantVitry["NO2"],'-*')
    plt.plot(DonneesPolluantVitry["NOX"],'-*')
    plt.plot(DonneesPolluantVitry["O3"],'-*')
    plt.plot(DonneesPolluantVitry["PM10"],'-*')
    plt.plot(DonneesPolluantVitry["PM2.5"],'-*')
    plt.title(f"Graphique linéaire de la mesure de chaque polluants en temps réel à Vitry-sur-Seine ({date})")
    plt.legend(["NO (monoxyde d’azote)","NO2 (dioxyde de carbone)","NOX (oxydes d'azote)","O3 (ozone)","PM10 (Particules de diamètre inférieur à 10 µm)","PM2.5(Particules de diamètre inférieur à 2.5 µm)"])
    plt.gca().xaxis.set_tick_params(labelsize = 7)
    plt.grid(which='major', axis='x', color='black', linestyle='dashed')
    plt.grid(which='major', axis='y', color='black', linestyle='dashed')
    plt.xlabel('Période (Heure)')
    plt.ylabel('Mesure en µg/m³')
    
    # Seuil de dépassement
    indicesNo2 = np.where(DonneesPolluantVitry["NO2"] > 40)[0]
    indicesNoX = np.where(DonneesPolluantVitry["NOX"] > 30)[0]
    indicesO3 = np.where(DonneesPolluantVitry["O3"] > 120)[0]
    indicesPM25 = np.where(DonneesPolluantVitry["PM2.5"] > 20)[0]
    indicesPM10 = np.where(DonneesPolluantVitry["PM10"] > 50)[0]
    
    # Ajout de l'alerte en cas de dépassement du seuil
    indice_mark(DonneesPolluantVitry,indicesO3,"O3")
    indice_mark(DonneesPolluantVitry,indicesNoX,"NOX")
    indice_mark(DonneesPolluantVitry,indicesNo2,"NO2")
    indice_mark(DonneesPolluantVitry,indicesPM25,"PM2.5")
    indice_mark(DonneesPolluantVitry,indicesPM10,"PM10")

    figure = plt.gcf()  # Graphique en mode plein écran
    figure.set_size_inches(16,9) 
    # Sauvegarde de la figure en plein écran
    output_path1 = os.path.join("static", "data_image.png")
    output_path2 = os.path.join("static", "data-graph.pdf")
    plt.savefig(output_path1, bbox_inches = 'tight', dpi = 300)
    plt.savefig(output_path2)
    plt.close()
    return