from rich.tree import Tree
from Modele import Ronde

# -----------------------------------------définition des constantes-------------------------------
GAGNER_MATCH = 1
PERDU_MATCH = 0
NUL_MATCH = 0.5
# -----------------------------------------définition de la classe---------------------------------


class Match:

    def __init__(self):
        self.score_match = []
        self.id_match = 0
        self.resultat_match = [GAGNER_MATCH, PERDU_MATCH, NUL_MATCH]
        self.joueur_resultat = 0

