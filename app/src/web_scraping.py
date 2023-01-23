import requests # Établir des requêtes HTTP en Python
from bs4 import BeautifulSoup # Extraction des données à partir d'un site web (web-scraping)

#URL vers la page regroupant toutes les données des polluants en 2021
u2021 = "https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/2021/"
#On convertit le lien de façon à ce qu'on puisse le manipuler à l'aide de modules Python
page1 = requests.get(u2021)
soup1 = BeautifulSoup(page1.content, "html.parser")


#URL vers la page regroupant toutes les données des polluants en 2022
u2022 = "https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/2022/"
#On convertit le lien de façon à ce qu'on puisse le manipuler à l'aide de modules Python
page2 = requests.get(u2022)
soup2 = BeautifulSoup(page2.content, "html.parser")



#URL vers la page regroupant toutes les données des polluants en 2023
u2023 = "https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/2023/"
#On convertit le lien de façon à ce qu'on puisse le manipuler à l'aide de modules Python
page3 = requests.get(u2023)
soup3 = BeautifulSoup(page3.content, "html.parser")

