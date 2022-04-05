# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from rich.tree import Tree
from rich.table import Table
from rich import box
#############################################

# Définition des constantes
GAGNER_MATCH = 1
PERDU_MATCH = 0
NUL_MATCH = 0.5
MATCH = 'Match'
COMPTEUR = 1
JOUEUR_A = 0
JOUEUR_B = 1
MATCH_NOM_JOUEUR = 1
BOLD = 'Bold'
NOM_JOUEUR_A = 'Joueur A'
NOM_JOUEUR_B = 'Joueur B'
VAINQUEUR = 'Vainqueur'

# Définition de la classe


class Match:

    def __init__(self):
        self.resultat_match = [PERDU_MATCH, GAGNER_MATCH, NUL_MATCH]
        self.arbre_match = Tree
        self.arbre_resultat_match = Tree
        self.tableau_ronde_match_tournoi = Table

    def creer_arbre_match(self, ronde, id_match) -> [Tree]:
        self.arbre_match = ronde.add(f'{MATCH}{id_match + COMPTEUR}')
        return self.arbre_match

    def utiliser_arbre_match(self) -> [Tree]:
        return self.arbre_match

    def cree_arbre_resultat_match(self, ronde, id_match) -> [Tree]:
        self.arbre_resultat_match = Tree(f'\n{MATCH}{id_match + 1}')
        self.arbre_resultat_match.add(f'{ronde[id_match][JOUEUR_A][MATCH_NOM_JOUEUR]}')
        self.arbre_resultat_match.add(f'{ronde[id_match][JOUEUR_B][MATCH_NOM_JOUEUR]}')
        return self.arbre_resultat_match

    def utiliser_arbre_resultat_match(self) -> [Tree]:
        return self.arbre_resultat_match

    def cree_tableau_ronde_match_tournoi(self, id_ronde) -> [Table]:
        self.tableau_ronde_match_tournoi = Table(box=box.HORIZONTALS, show_header=True, header_style=BOLD,
                                                 title=id_ronde)
        self.tableau_ronde_match_tournoi.add_column(MATCH)
        self.tableau_ronde_match_tournoi.add_column(NOM_JOUEUR_A)
        self.tableau_ronde_match_tournoi.add_column(NOM_JOUEUR_B)
        self.tableau_ronde_match_tournoi.add_column(VAINQUEUR)
        return self.tableau_ronde_match_tournoi

    def utiliser_tableau_ronde_match_tournoi(self) -> [Table]:
        return self.tableau_ronde_match_tournoi
