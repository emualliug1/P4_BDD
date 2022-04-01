#Projet 4
###Développez un programme logiciel en Python

##Création d'un programme qui gere un tournoi d'echec :
###Déroulement de base du tournoi :
    1. Créer un nouveau tournoi.
    2. Ajouter huit joueurs.
    3. L'ordinateur génère des paires de joueurs pour le premier tour.
    4. Lorsque le tour est terminé, entrez les résultats.
    5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.

###Schéma des tournois :
    -Nom
    -Lieu
    -Date
    -Nombre de tours
    -Rondes
    -Joueurs
    -Contrôle du temps
    -Description

###Programme des joueurs :
    -Nom de famille
    -Prénom
    -Date de naissance
    -Sexe
    -Clasement

###Rondes/Matchs:



## Commencer :
Assurez-vous que python est installé sur votre machine :
 
    python -V

Vérifiez que vous disposez du module venv :
    
    python -m venv --help
  
Si Python n'est pas installé sur votre machine :
    
    https://www.python.org/downloads/
    
Si vous ne disposez pas du module virtual env:
    
    py -m pip install --user virtualenv
    

###Une fois Python installé :
   
 Ouvrir une invite de commande et utiliser la commande :`cd` pour aller dans le repertoire ou vous voulez copier le projet. 
    Vous pouvez aussi créer un nouveau repertoire avec la commande: `mkdir`
    Une fois dans le bon repertoire il vous suffit de taper: 
 
    git clone https://github.com/emualliug1/P4_BDD
    
Créer un environnement virtuel avec venv :`python -m venv ***nom de l'environnement***` : pour créer l'environnement virtuel --- exemple : 

    py -m venv env
    
Activez l'environnement virtuel : `***nom de l'environnement***/Scripts/activate.bat` --- exemple : 

    env/Scripts/activate.bat
    
Installez les packages avec pip: 

    pip install -r requirements.txt

Lancez le programme avec : 

    python main.py

