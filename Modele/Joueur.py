# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from rich.table import Table
from rich import box
#############################################

# Définition des constantes
NOM = 'Nom'
PRENOM = 'Prenom'
DATE_NAISSANCE = 'Date de naissance'
SEXE = 'Sexe'
CLASSEMENT = 'Classement'
COMPTEUR = 1
BOLD = "bold"
TITRE_TABLEAU_JOUEURS = "Joueurs enregistré"
ID = 'ID'

# Définition de la classe


class Joueur:
    """Description d'une classe joueur"""

    SEXE = ['Masculin', 'Feminin']

    def __init__(self):
        self.nom_famille = ''
        self.prenom = ''
        self.date_naissance = ''
        self.sexe = 0
        self.classement = 0
        self.dict_id_joueur = 0
        self.id_joueur = 0
        self.tableau_joueurs = Table
        self.dict_joueur = {}


    def creer_tableau_joueur(self) -> [Table]:
        self.tableau_joueurs = Table(box=box.HORIZONTALS,
                                     show_header=True,
                                     header_style=BOLD,
                                     title=TITRE_TABLEAU_JOUEURS)

        self.tableau_joueurs.add_column(ID)
        self.tableau_joueurs.add_column(NOM)
        self.tableau_joueurs.add_column(PRENOM)
        self.tableau_joueurs.add_column(DATE_NAISSANCE)
        self.tableau_joueurs.add_column(SEXE)
        self.tableau_joueurs.add_column(CLASSEMENT)

        return self.tableau_joueurs

    def utiliser_tableau_joueur(self):
        return self.tableau_joueurs

    def dictionnaire_joueur(self):
        self.nom_famille = self.nom_famille.upper()
        self.prenom = self.prenom.capitalize()
        self.sexe = Joueur.SEXE[self.sexe]
        self.dict_joueur = {
            NOM: self.nom_famille,
            PRENOM: self.prenom,
            DATE_NAISSANCE: self.date_naissance,
            SEXE: self.sexe,
            CLASSEMENT: self.classement}
        return self.dict_joueur
