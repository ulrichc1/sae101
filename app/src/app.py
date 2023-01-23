from web_scraping import *
from lectureCSV import *
from visualisation import *
from graphs import *
from pdfFiles import *

def montrerGraphique(date,resultat):
    """ str, DataFrame -> None
    Préconditions : les fonctions CreateDataframe et CreateDescribeData doivent exister
    Rôle: Trace et montre le graphique correspondant à la mesure de chaque polluants à Vitry-sur-Seine"""
    DonneesPolluantVitry = CreateDataframe(resultat)
    print("\n")
    print(DonneesPolluantVitry)
    print("\n")
    print(CreateDescribeData(DonneesPolluantVitry))
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
    plt.show()
    return


def run():
    """None -> None
    Préconditions : -
    Rôle : Exécutes l'analyse de données en fonction de la date saisie par l'utilisateur dans le format respecté, le cas échéant exécutes l'analyse de données pour le dernier relevé présent à ce jour"""
    listeCSV = find_allCSV(soup1) + find_allCSV(soup2) + find_allCSV(soup3)
    print(f"Données disponibles du {listeCSV[0].split('_')[2]} au {listeCSV[-1].split('_')[2]}")
    date = str(input("Veuillez saisir une date au format YYYY-MM-DD: "))
    if(readDateCSV(date)) is not None: #Si la date a été trouvé dans la liste des csv disponibles, alors exécuter l'analyse pour la date donnée
        data = (readDateCSV(date))
        montrerGraphique(date,data)
    else: #Sinon exécuter l'analyse pour le dernier relevé présent à ce jour
        date = f"{listeCSV[-1].split('_')[2].split('.')[0]}"
        data2 = readLastCSV()
        montrerGraphique(date,data2)
    return
        
        
    
