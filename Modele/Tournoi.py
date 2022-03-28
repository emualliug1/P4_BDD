
from rich.table import Table
from rich import box

# -----------------------------------------définition des constantes-------------------------------
NOM = 'Nom'
LIEU = 'Lieu'
DATE_TOURNOI = 'Date du tournoi'
CONTROLE_TEMPS = 'Controle du temps'
DESCRIPTION = 'Description'
JOUEURS_TOURNOI = 'Joueurs du tournoi'
COMPTEUR = 1
BOLD = "bold"
TITRE_TABLEAU_TOURNOI = "Tournoi enregistré"
ID = 'ID'

# -----------------------------------------définition de la classe---------------------------------


class Tournoi:
    """Description d'une classe tournoi"""
    CONTROLE_TEMPS = ["Bullet", "Blitz", "Coup Rapide"]

    def __init__(self,
                 ronde,
                 nom=None,
                 lieu=None,
                 date=None,
                 controle_temps=None,
                 description=None,
                 nombre_ronde_max=4,
                 nombre_joueur_max=8):
        self.nom_tournoi = nom
        self.lieu = lieu
        self.date_tournoi = date
        self.controle_temps = controle_temps
        self.description = description
        self.rondes_max = nombre_ronde_max
        self.joueurs_max = nombre_joueur_max
        self.dict_tournoi = {}
        self.joueurs_tournoi = []
        self.id_tournoi = 0
        self.joueurs_trier_classement = []
        self.tableau_tournoi = Table
        self.ronde = ronde

    def enregistrer_tournoi(self, numero) -> [dict]:
        """Enregistrement d'un tournoi"""
        self.nom_tournoi = self.nom_tournoi.upper()
        self.lieu = self.lieu.upper()
        self.description = self.description.capitalize()
        self.controle_temps = Tournoi.CONTROLE_TEMPS[self.controle_temps]
        self.id_tournoi += COMPTEUR

        self.dict_tournoi[numero] = {
            NOM: self.nom_tournoi,
            LIEU: self.lieu,
            DATE_TOURNOI: self.date_tournoi,
            CONTROLE_TEMPS: self.controle_temps,
            DESCRIPTION: self.description,
            JOUEURS_TOURNOI: self.joueurs_tournoi
        }

        return self.dict_tournoi

    def enregistrer_ronde(self, id_tournoi) -> [list]:
        """Enregistre une ronde dans un dictionnaire"""
        self.dict_tournoi[id_tournoi][self.ronde.id_ronde] = self.ronde.ronde_liste
        return self.ronde.ronde_liste

    def enregistrer_joueurs_tournoi(self, id_tournoi) -> [list]:
        """Enregistre les joueurs du tournoi dans un dictionnaire"""
        self.dict_tournoi[id_tournoi][JOUEURS_TOURNOI] = self.joueurs_tournoi
        return self.joueurs_tournoi

    def utiliser_id_tournoi(self):
        return self.id_tournoi

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

    def utiliser_tableau_tournoi(self):
        return self.tableau_tournoi

    def ajouter_tournoi_dict(self, id_tournoi, nom, lieu, date, controle_temps, description) -> [dict]:
        """Créer un tournoi fictif comme exemple"""
        self.dict_tournoi[id_tournoi] = {
            NOM: nom,
            LIEU: lieu,
            DATE_TOURNOI: date,
            CONTROLE_TEMPS: controle_temps,
            DESCRIPTION: description}

        return self.dict_tournoi
