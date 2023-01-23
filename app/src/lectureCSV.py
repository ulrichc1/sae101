import pandas as pd # Lecture de .csv vers DataFrame
from web_scraping import *

# Récupération des liens .csv
def find_allCSV(site):
    """BeautifulSoup -> list[str]
       Préconditions : Le site doit inclure des liens (href) dirigeant vers des fichiers .csv
       Rôle : Trouve tous les liens vers des fichiers .csv et les range dans une liste"""
    links = site.find_all("a") # Cherche tous les liens de la page
    # Liste par compréhension cherchant si un lien contient un fichier .csv et l'ajoutant à une liste
    return [str(link.text.strip()) for link in links if ("csv" in str(link.text.strip()))]

# Lecture du dernier lien .csv
def readLastCSV():
    """ None -> DataFrame
       Préconditions : Le site doit inclure des liens (href) dirigeant vers des fichiers .csv
       Rôle : Lit le dernier lien .csv des fichiers .csv de 2023"""
    landing = "https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/2023/"
    liste = find_allCSV(soup3) #Appel de la fonction précédente
    liste.reverse() #On renverse la liste afin d'avoir le dernier lien en premier
    url = landing + liste[0] #On construit l'url permettant au module panda de lire le fichier .csv à partir du dernier jour
    df = pd.read_csv(url, sep=';')  #On lit l'url
    return df

def findDate(date,liste):
    """str,list[str] -> DataFrame
       Préconditions : -
       Rôle : Trouve la date passé en paramètre dans la liste des fichiers .csv et retourne le DataFrame correspondant au .csv trouvé"""
    landing = f'https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/{date.split("-")[0]}/'
    for i, chaine in enumerate(liste): #On parcours la liste des fichiers CSV ainsi que leur position dans la liste
        position = chaine.find(date) #On regarde si la date indiquée existe dans la liste
        if position != -1: #Si oui on lit le fichier CSV correspondant à la date indiquée
            url = landing + liste[i] #On construit l'url permettant au module panda de lire le fichier .csv à partir du dernier jour
            df = pd.read_csv(url, sep=';')  #On lit l'url
    return df
            
def readDateCSV(date):
    """str -> DataFrame
       Préconditions : Le site doit inclure des liens (href) dirigeant vers des fichiers .csv et la date doit être au format AAAA-MM-DD
       Rôle : Renvoie le DataFrame correspondant à la date passé en paramètre"""
    listeCSV2021 = find_allCSV(soup1)
    listeCSV2022 = find_allCSV(soup2)
    listeCSV2023 = find_allCSV(soup3)
    if (date.split("-")[0]=="2021"):
        return findDate(date,listeCSV2021)
    elif (date.split("-")[0]=="2022"):
        return findDate(date,listeCSV2022)
    elif (date.split("-")[0]=="2023"):
        return findDate(date,listeCSV2023)
    else:
        return