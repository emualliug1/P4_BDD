from rich.table import Table
from rich import box

# -----------------------------------------définition des constantes-------------------------------
NOM = 'Nom'
PRENOM = 'Prenom'
DATE_NAISSANCE = 'Date de naissance'
SEXE = 'Sexe'
CLASSEMENT = 'Classement'
COMPTEUR = 1
BOLD = "bold"
TITRE_TABLEAU_JOUEURS = "Joueurs enregistré"
ID = 'ID'
# -----------------------------------------définition de la classe---------------------------------


class Joueur:
    """Description d'une classe joueur"""
    SEXE = ['Masculin', 'Féminin']

    def __init__(self,
                 nom=None,
                 prenon=None,
                 date_naissance=None,
                 sexe=None,
                 classement=None):
        self.nom_famille = nom
        self.prenom = prenon
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.dict_joueurs = {}
        self.dict_id_joueur = 0
        self.id_joueur = 0
        self.tableau_joueurs = Table

    def enregistrer_joueur(self, numero) -> [dict]:
        """Enregistrement d'un joueur"""
        self.dict_id_joueur += COMPTEUR
        self.nom_famille = self.nom_famille.upper()
        self.prenom = self.prenom.capitalize()
        self.sexe = Joueur.SEXE[self.sexe]

        self.dict_joueurs[numero] = {
            NOM: self.nom_famille,
            PRENOM: self.prenom,
            DATE_NAISSANCE: self.date_naissance,
            SEXE: self.sexe,
            CLASSEMENT: self.classement
        }

        return self.dict_joueurs

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

    def ajouter_joueur_dict(self, id_joueur, nom, prenom, date_naissance, sexe, classement) -> [dict]:
        """Créer un joueur fictif comme exemple"""
        self.dict_joueurs[id_joueur] = {
            NOM: nom,
            PRENOM: prenom,
            DATE_NAISSANCE: date_naissance,
            SEXE: sexe,
            CLASSEMENT: classement}

        return self.dict_joueurs
