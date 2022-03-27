from rich import box
from rich.tree import Tree
from rich.table import Table
# -----------------------------------------définition des constantes-------------------------------
ID = 'ID'
NOM = 'Nom'
CLASSEMENT = 'Classement'
SCORES_RONDES = "Scores rondes"
SCORE_TOURNOI = "Score du tournoi"
RONDE = 'Ronde'
MATCH = 'Match'
BOLD = "bold"
# -----------------------------------------définition de la classe---------------------------------


class Ronde:

    def __init__(self):
        self.nom_du_tour = ''
        self.date_du_tour = ''
        self.heure_du_tour = ''
        self.liste_match = []
        self.joueurs_a = []
        self.joueurs_b = []
        self.ronde = []
        self.dict_ronde = {}
        self.id_compteur = 0
        self.id_ronde = ''
        self.ronde_tree = Tree
        self.match_tree = Tree
        self.table_resultat_ronde = Table
        self.table_ronde = Table
        self.table_match = Table

    def creer_tableau_ronde(self):
        self.table_resultat_ronde = Table(box=box.HORIZONTALS, show_header=True, header_style=BOLD,
                                          title=self.id_ronde)
        self.table_resultat_ronde.add_column(ID)
        self.table_resultat_ronde.add_column(NOM)
        self.table_resultat_ronde.add_column(CLASSEMENT)
        self.table_resultat_ronde.add_column(SCORES_RONDES)
        self.table_resultat_ronde.add_column(SCORE_TOURNOI)

        return self.table_resultat_ronde

    def creer_arbre_ronde(self):
        self.id_compteur += 1
        self.id_ronde = f'{RONDE}{self.id_compteur}'
        self.ronde_tree = Tree(label=self.id_ronde)
        return self.ronde_tree

    def creer_arbre_match(self, id_match):
        self.match_tree = self.creer_arbre_ronde().add(f'{MATCH}{id_match + 1}')
        return self.match_tree

    def cree_arbre_resultat_match(self, id_match):
        self.match_tree = Tree(f'\n{MATCH}{id_match + 1}')
        self.match_tree.add(f'{self.ronde[id_match][0][1]}')
        self.match_tree.add(f'{self.ronde[id_match][1][1]}')
        return self.match_tree
