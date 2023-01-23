from lectureCSV import *

# Récupération de chaque indice des lignes correspondantes aux données présentes à Vitry-sur-Seine
def donneesAVitry(data,cle):
  """DataFrame,str -> list[int]
     Préconditions : -
     Rôle : Récupère et retourne un tableau comportant les indices de chaque lignes correspondantes à la ville de Vitry-sur-Seine dans un DataFrame"""    
  return [k for k in range(len(data)) if (data[cle][k]=='VITRY-SUR-SEINE')] 

# Mesures brutes des polluants demandés réalisés à Vitry-sur-Seine    
def mesuresBrutesPolluants(data,cle,polluant):
    """DataFrame,str,str -> list[float]
     Préconditions : La fonction donneesAVitry(data,city_key) doit exister
     Rôle : Récupère et retourne la liste des mesures brutes du polluant passé en paramètre à Vitry-sur-Seine"""   
    return [data["valeur brute"][i] for i in donneesAVitry(data,"nom site") if (data[cle][i] == polluant)]

#On récupère les dates de mesures de polluants (apriori les mesures de chaques polluants ont été effectués au même moment)
def DateDebutMesure(data,cle,polluant):
    """DataFrame,str,str -> list[str]
     Préconditions : La fonction donneesAVitry(data,city_key) doit exister
     Rôle : Récupère et retourne la liste des dates de mesures du polluant passé en paramètre à Vitry-sur-Seine"""   
    return [data[cle][i].split(" ")[-1] for i in donneesAVitry(data,"nom site") if data["Polluant"][i]==polluant]


def CreateDataframe(resultat):
    """DataFrame -> DataFrame
     Préconditions : La fonction DateDebutMesure et mesuresBrutesPolluants doivent exister
     Rôle : Renvoie un nouveau DataFrame représentant les mesures brutes des polluants avec leurs dates correspondantes"""   
    # Création d'un second DataFrame représentant la mesure brute des polluants présents à Vitry-sur-Seine par date de mesure
    #Stockage des mesures brutes des polluants demandés réalisés à Vitry-sur-Seine
    date_key = "Date de début"
    polluant_key = "Polluant"
    mesuresNO = mesuresBrutesPolluants(resultat,polluant_key,'NO')
    mesuresNO2 = mesuresBrutesPolluants(resultat,polluant_key,'NO2')
    mesuresNOX = mesuresBrutesPolluants(resultat,polluant_key,'NOX as NO2')
    mesuresO3 = mesuresBrutesPolluants(resultat,polluant_key,'O3')
    mesuresPM10 = mesuresBrutesPolluants(resultat,polluant_key,'PM10')
    mesuresPM25 = mesuresBrutesPolluants(resultat,polluant_key,'PM2.5')
    DonneesPolluantVitry = pd.DataFrame({'NO': mesuresNO, 'NO2': mesuresNO2, 'NOX': mesuresNOX, 'O3': mesuresO3,'PM10': mesuresPM10,'PM2.5': mesuresPM25},
                      index = DateDebutMesure(resultat,date_key,'NO')) #Création du DataFrame
    return DonneesPolluantVitry

def CreateDescribeData(dataframe):
    """DataFrame -> DataFrame
     Préconditions : -
     Rôle : Renvoie un DataFrame détaillé avec minimum, maximum, écart-type et moyenne de données de chaques polluants"""   
    return dataframe.describe() 

