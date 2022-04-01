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
LIEU = 'Lieu'
DATE_TOURNOI = 'Date du tournoi'
CONTROLE_TEMPS = 'Controle du temps'
DESCRIPTION = 'Description'
JOUEURS_TOURNOI = 'Joueurs du tournoi'
COMPTEUR = 1
BOLD = 'bold'
TITRE_TABLEAU_TOURNOI = 'Tournoi enregistré'
ID = 'ID'
PRENOM = 'Prenom'
DATE_NAISSANCE = 'Date de naissance'
SEXE = 'Sexe'
CLASSEMENT = 'Classement'

# Définition de la classe


class Tournoi:
    """Description d'une classe tournoi"""
    CONTROLE_TEMPS = ["Bullet", "Blitz", "Coup Rapide"]

    def __init__(self,
                 nombre_ronde_max=4,
                 nombre_joueur_max=8):
        self.nom_tournoi = ''
        self.lieu = ''
        self.date_tournoi = ''
        self.controle_temps = 0
        self.description = ''
        self.rondes_max = nombre_ronde_max
        self.joueurs_max = nombre_joueur_max
        self.joueurs_tournoi = []
        self.id_tournoi = 0
        self.joueurs_trier_classement = []
        self.tableau_tournoi = Table
        self.tableau_joueurs_tournoi = Table
        self.dict_tournoi = {}

    def dictionnaire_tournoi(self) -> [dict]:
        self.nom_tournoi = self.nom_tournoi.upper()
        self.lieu = self.lieu.upper()
        self.description = self.description.capitalize()
        self.controle_temps = Tournoi.CONTROLE_TEMPS[self.controle_temps]
        self.dict_tournoi = {NOM: self.nom_tournoi,
                             LIEU: self.lieu,
                             DATE_TOURNOI: self.date_tournoi,
                             CONTROLE_TEMPS: self.controle_temps,
                             DESCRIPTION: self.description,
                             JOUEURS_TOURNOI: self.joueurs_tournoi}
        return self.dict_tournoi

    def creer_tableau_tournoi(self) -> [Table]:
        self.tableau_tournoi = Table(box=box.HORIZONTALS,
                                     show_header=True,
                                     header_style=BOLD,
                                     title=TITRE_TABLEAU_TOURNOI)
        self.tableau_tournoi.add_column(ID)
        self.tableau_tournoi.add_column(NOM)
        self.tableau_tournoi.add_column(LIEU)
        self.tableau_tournoi.add_column(CONTROLE_TEMPS)
        self.tableau_tournoi.add_column(DATE_TOURNOI)
        self.tableau_tournoi.add_column(DESCRIPTION)
        return self.tableau_tournoi

    def utiliser_tableau_tournoi(self) -> [Table]:
        return self.tableau_tournoi

    def utiliser_id_tournoi(self) -> [int]:
        return self.id_tournoi

    def creer_tableau_joueurs_tournoi(self) -> [Table]:
        self.tableau_joueurs_tournoi = Table(box=box.HORIZONTALS,
                                             show_header=True,
                                             header_style=BOLD,
                                             title=JOUEURS_TOURNOI)
        self.tableau_joueurs_tournoi.add_column(ID)
        self.tableau_joueurs_tournoi.add_column(NOM)
        self.tableau_joueurs_tournoi.add_column(CLASSEMENT)
        return self.tableau_joueurs_tournoi

    def utiliser_tableau_joueurs_tournoi(self) -> [Table]:
        return self.tableau_joueurs_tournoi
