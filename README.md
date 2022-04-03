# Projet 4
## Programme de gestion d'un tournoi d'échec

### Objectif :
Étape 1 : Se familiariser avec les classes et la programmation orientée objet.

Étape 2 : Définir et coder les modèles pour ce projet.

Étape 3 : Mettre en œuvre la conception MVC.

Étape 4 : Implémenter la sérialisation.

### Commencer :
Assurez-vous que python est installé sur votre machine :

    python -V

Vérifiez que vous disposez du module venv :
    
    python -m venv --help
  
Si Python n'est pas installé sur votre machine :
    
    https://www.python.org/downloads/
    
Si vous ne disposez pas du module virtual env:
    
    py -m pip install --user virtualenv
    

### Une fois Python installé :
   
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

creer un rapport flake8 :

    flake8 --format=html --htmldir=flake-report

### Fonctionnement :
1)Ajouter des joueurs dans la BDD :

![Imgur](https://i.imgur.com/AVCcB1E.png) 
![Imgur](https://i.imgur.com/CUlzFrU.png)
![Imgur](https://i.imgur.com/ayRXqEk.png)

2) Ajouter un tournoi dans la BDD :

![Imgur](https://i.imgur.com/AVCcB1E.png)
![Imgur](https://i.imgur.com/UDwFA5f.png)
![Imgur](https://i.imgur.com/PTgryYg.png)

#### Quand vous avez ajoutés 8 joueurs vous pouvez lancer un tournoi :

![Imgur](https://i.imgur.com/AVCcB1E.png)
![Imgur](https://i.imgur.com/UDwFA5f.png)
![Imgur](https://i.imgur.com/D1fixml.png)

1) Choisir un tournoi dans ceux enregistré dans la BDD

![Imgur](https://i.imgur.com/DzciBwx.png)

2) Entrer 8 joueurs au tournoi

![Imgur](https://i.imgur.com/0Z5haAR.png)

3) Affichage de la ronde

![Imgur](https://i.imgur.com/9RoxyoC.png)

4) Entrer le vainqueur du match

![Imgur](https://i.imgur.com/JtDOD0I.png)

5) Tableau récapitulatif à chaque fin de ronde

![Imgur](https://i.imgur.com/cu7n71v.png)


