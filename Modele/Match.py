# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from rich.tree import Tree
#############################################

# Définition des constantes
GAGNER_MATCH = 1
PERDU_MATCH = 0
NUL_MATCH = 0.5
MATCH = 'Match'
COMPTEUR = 1

# Définition de la classe


class Match:

    def __init__(self):
        self.score_match = []
        self.id_match = 0
        self.resultat_match = [GAGNER_MATCH, PERDU_MATCH, NUL_MATCH]
        self.joueur_resultat = 0
        self.arbre_match = Tree
        self.arbre_resultat_match = Tree

    def creer_arbre_match(self, ronde, id_match) -> [Tree]:
        self.arbre_match = ronde.add(f'{MATCH}{id_match + COMPTEUR}')
        return self.arbre_match

    def utiliser_arbre_match(self) -> [Tree]:
        return self.arbre_match

    def cree_arbre_resultat_match(self, ronde, id_match) -> [Tree]:
        self.arbre_resultat_match = Tree(f'\n{MATCH}{id_match + 1}')
        self.arbre_resultat_match.add(f'{ronde[id_match][0][1]}')
        self.arbre_resultat_match.add(f'{ronde[id_match][1][1]}')
        return self.arbre_resultat_match

    def utiliser_arbre_resultat_match(self) -> [Tree]:
        return self.arbre_resultat_match
