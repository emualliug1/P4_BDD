from Modele import Joueur
from Modele import Tournoi

# -----------------------------------------définition des constantes-------------------------------
ODRE_TRI = 1
NOM = 'Nom'
PRENOM = 'Prenom'
LIEU = 'Lieu'
CONTROLE_TEMPS = 'Controle du temps'
SEXE = 'Sexe'
DATE_NAISSANCE = 'Date de naissance'
CLASSEMENT = 'Classement'
DATE_TOURNOI = 'Date du tournoi'
DESCRIPTION = 'Description'

# -----------------------------------------définition de la classe---------------------------------


class Controleur:

    def __init__(self, vue, tournoi, joueur, ronde, match):
        self.vue = vue
        self.tournoi = tournoi
        self.joueur = joueur
        self.ronde = ronde
        self.match = match

    @staticmethod
    def trier_dict(dictionnaire, trie):
        dict_trier_classement = dict(sorted(dictionnaire.items(),
                                            key=lambda x: (x[ODRE_TRI][trie])))
        return dict_trier_classement

    def recuperer_information_joueur(self):
        nom = self.vue.entrer_nom_joueur()
        prenom = self.vue.entrer_prenom_joueur()
        date_naissance = self.vue.entrer_date_naissance_joueur()
        sexe = self.vue.entrer_sexe_joueur()
        classement = self.vue.entrer_classement_joueur()
        joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
        return joueur

    def recuperer_information_tournoi(self):
        nom = self.vue.entrer_nom_tournoi()
        lieu = self.vue.entrer_lieu_tournoi()
        date_tournoi = self.vue.entrer_date_tournoi()
        controle_temps = self.vue.entrer_controle_temps_tournoi()
        description = self.vue.entrer_description_tournoi()
        tournoi = Tournoi(nom, lieu, date_tournoi, controle_temps, description)
        return tournoi

    def recuperer_joueurs_trier_tableau(self, trie):
        self.joueur.creer_tableau_joueur()
        for id_joueurs in self.trier_dict(self.joueur.dict_joueurs, trie).keys():
            self.joueur.utiliser_tableau_joueur().add_row(str(id_joueurs),
                                                       self.joueur.dict_joueurs[id_joueurs][NOM],
                                                       self.joueur.dict_joueurs[id_joueurs][PRENOM],
                                                       self.joueur.dict_joueurs[id_joueurs][DATE_NAISSANCE],
                                                       self.joueur.dict_joueurs[id_joueurs][SEXE],
                                                       str(self.joueur.dict_joueurs[id_joueurs][CLASSEMENT]))
        return self.joueur.utiliser_tableau_joueur()

    def recuperer_tournois_trier_tableau(self, trie):
        self.tournoi.creer_tableau_tournoi()
        for id_tournoi in self.trier_dict(self.tournoi.dict_tournoi, trie).keys():
            self.tournoi.utiliser_tableau_tournoi().add_row(str(id_tournoi),
                                                         self.tournoi.dict_tournoi[id_tournoi][NOM],
                                                         self.tournoi.dict_tournoi[id_tournoi][LIEU],
                                                         self.tournoi.dict_tournoi[id_tournoi][CONTROLE_TEMPS],
                                                         self.tournoi.dict_tournoi[id_tournoi][DATE_TOURNOI],
                                                         str(self.tournoi.dict_tournoi[id_tournoi][DESCRIPTION]))
        return self.tournoi.utiliser_tableau_tournoi()

    

