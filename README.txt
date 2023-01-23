SAE 1.01 - Implémentation d'un besoin client
BUT INFORMATIQUE
GROUPE B:
COUDIN Ulrich - COQUERELLE Mélissa - LAMARQUE Noé - MOLINIER Hugo


/**** INSTALLER IMPÉRATIVEMENT CES MODULES AVANT D'UTILISER LE LOGICIEL *****/
- os
- matplotlib
- pandas
- numpy
- requests
- bs4
- tabulate
- fpdf
- pdfrw
- Flask
- flask_request_arg

/****************************************************************************/

Afin de pouvoir utiliser le logiciel sans interface Web :

Il vous suffit d'ouvrir le fichier " run.py " dans le dossier 'app/src' et exécuter le programme (pensez à bien lire les commentaires et instructions dans la console).

Afin de pouvoir utiliser le logiciel avec interface web :

Il vous suffit d'ouvrir le fichier " main.py " dans le dossier 'app/src' et exécuter le programme (pensez à bien lire les commentaires et instructions)
Le lien afin d'accéder au serveur Flask de la page web devrait être : http://127.0.0.1:5000/

/*****************************************************************************/

Veuillez noter que l'exécution du logiciel sur le site web peut être lent (20s à 1 minute d'attente)
Certains problèmes peuvent également apparaître lorsque on réalise plusieurs analyses de manières successives sur le site web, pensez à rafraichir la page vers le lien indiqué plus au-dessus 
afin de pouvoir effectuer de nouvelles analyses, ou bien stopper l'exécution du serveur Flask et relancez-le toujours en suivant les instructions plus au dessus.

/*****************************************************************************/

L'ensemble des fichiers se trouve dans le répertoire '/app'.
Afin d'accéder aux fichiers sources (codes, modules...) du logiciel il vous suffit de vous rendre dans le répertoire '/src'.
Les fichiers correspondant au site web (en .html), au style (.css) et au script Javascript (.js) de la page web sont respectivements dans les répertoires '/templates' et '/static'.


/*****************************************************************************/

Le répertoire '/synthese' contient la fiche de synthèse de chaques fonctions créees.
La vidéo de démonstration du site web est présent sur le second livrable qui vous a été fourni, à savoir le Powerpoint sonorisé (au format .pptx).