# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from rich import box
from rich.tree import Tree
from rich.table import Table
#############################################
# Définition des constantes
ID = 'ID'
NOM = 'Nom'
CLASSEMENT = 'Classement'
SCORES_RONDES = 'Scores rondes'
SCORE_TOURNOI = 'Score du tournoi'
RONDE = 'Ronde'
MATCH = 'Match'
BOLD = 'bold'

# Définition de la classe


class Ronde:

    def __init__(self):
        self.joueurs_a = []
        self.joueurs_b = []
        self.ronde_liste = []
        self.id_compteur = 0
        self.id_ronde = ''
        self.arbre_ronde = Tree
        self.arbre_ronde_match = Tree
        self.tableau_resultat_ronde = Table
        self.tableau_ronde = Table
        self.tableau_match = Table

    def creer_tableau_ronde(self) -> [Table]:
        self.tableau_resultat_ronde = Table(box=box.HORIZONTALS, show_header=True, header_style=BOLD,
                                            title=self.id_ronde)
        self.tableau_resultat_ronde.add_column(ID)
        self.tableau_resultat_ronde.add_column(NOM)
        self.tableau_resultat_ronde.add_column(CLASSEMENT)
        self.tableau_resultat_ronde.add_column(SCORES_RONDES)
        self.tableau_resultat_ronde.add_column(SCORE_TOURNOI)
        return self.tableau_resultat_ronde

    def utiliser_tableau_ronde(self) -> [Table]:
        return self.tableau_resultat_ronde

    def creer_arbre_ronde(self) -> [Tree]:
        self.id_compteur += 1
        self.id_ronde = f'{RONDE}{self.id_compteur}'
        self.arbre_ronde = Tree(label=self.id_ronde)
        return self.arbre_ronde

    def utiliser_arbre_ronde(self) -> [Tree]:
        return self.arbre_ronde

    def recuperer_vainqueur_tournoi(self):
        return self.ronde_liste[0][1]
