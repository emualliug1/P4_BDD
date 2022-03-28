# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from Modele import Joueur
from Modele import Tournoi
from operator import itemgetter
#############################################

# Définition des constantes
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
TRIE_CLASSEMENT = 2
TRIE_VICTOIRE = 3

# Définition de la classe


class Controleur:

    def __init__(self, vue, tournoi, joueur, ronde, match):
        self.vue = vue
        self.tournoi = tournoi
        self.joueur = joueur
        self.ronde = ronde
        self.match = match

    @staticmethod
    def trier_dict(dictionnaire, trie, reverse=False):
        dict_trier_classement = dict(sorted(dictionnaire.items(), reverse=reverse,
                                            key=lambda x: (x[ODRE_TRI][trie])))
        return dict_trier_classement

    def recuperer_information_joueur(self):
        self.vue.effacer_ecran()
        nom = self.vue.entrer_nom_joueur()
        prenom = self.vue.entrer_prenom_joueur()
        date_naissance = self.vue.entrer_date_naissance_joueur()
        sexe = self.vue.entrer_sexe_joueur()
        classement = self.vue.entrer_classement_joueur()
        joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
        return joueur

    def recuperer_information_tournoi(self):
        self.vue.effacer_ecran()
        nom = self.vue.entrer_nom_tournoi()
        lieu = self.vue.entrer_lieu_tournoi()
        date_tournoi = self.vue.entrer_date_tournoi()
        controle_temps = self.vue.entrer_controle_temps_tournoi()
        description = self.vue.entrer_description_tournoi()
        tournoi = Tournoi(nom, lieu, date_tournoi, controle_temps, description)
        return tournoi

    def modifier_joueur(self):
        """"Modification d'un joueur"""
        self.vue.effacer_ecran()
        self.vue.afficher_joueur_tableau(self.recuperer_joueur_tableau(NOM))
        joueur_id = self.vue.entrer_id()
        validation = self.vue.entrer_validation()
        if validation:
            self.recuperer_information_joueur()
            self.joueur.enregistrer_joueur(joueur_id)
        if not validation:
            self.vue.afficher_modification_annule()
            self.vue.pause_ecran()

    def modifier_tournoi(self):
        """"Modifier un tournoi enregistré"""
        self.vue.effacer_ecran()
        self.vue.afficher_tournoi_tableau(self.recuperer_tournoi_tableau(NOM))
        tournoi_id = self.vue.entrer_id()
        validation = self.vue.entrer_validation()
        if validation:
            self.recuperer_information_tournoi()
            self.tournoi.enregistrer_tournoi(tournoi_id)
        if not validation:
            self.vue.afficher_modification_annule()
            self.vue.pause_ecran()

    def recuperer_joueur_tableau(self, trie, reverse=False):
        self.joueur.creer_tableau_joueur()
        for id_joueurs in self.trier_dict(self.joueur.dict_joueurs, trie, reverse).keys():
            self.joueur.utiliser_tableau_joueur().add_row(str(id_joueurs),
                                                          self.joueur.dict_joueurs[id_joueurs][NOM],
                                                          self.joueur.dict_joueurs[id_joueurs][PRENOM],
                                                          self.joueur.dict_joueurs[id_joueurs][DATE_NAISSANCE],
                                                          self.joueur.dict_joueurs[id_joueurs][SEXE],
                                                          str(self.joueur.dict_joueurs[id_joueurs][CLASSEMENT]))
        return self.joueur.utiliser_tableau_joueur()

    def recuperer_tournoi_tableau(self, trie):
        self.tournoi.creer_tableau_tournoi()
        for id_tournoi in self.trier_dict(self.tournoi.dict_tournoi, trie).keys():
            self.tournoi.utiliser_tableau_tournoi().add_row(str(id_tournoi),
                                                            self.tournoi.dict_tournoi[id_tournoi][NOM],
                                                            self.tournoi.dict_tournoi[id_tournoi][LIEU],
                                                            self.tournoi.dict_tournoi[id_tournoi][CONTROLE_TEMPS],
                                                            self.tournoi.dict_tournoi[id_tournoi][DATE_TOURNOI],
                                                            str(self.tournoi.dict_tournoi[id_tournoi][DESCRIPTION]))
        return self.tournoi.utiliser_tableau_tournoi()

    def recuperer_ronde_tableau(self):
        self.ronde.creer_tableau_ronde()
        for joueur in self.ronde.ronde_liste:
            self.ronde.utiliser_tableau_ronde().add_row(
                                                        str(joueur[0]),
                                                        str(joueur[1]),
                                                        str(joueur[2]),
                                                        str(joueur[3]),
                                                        str(joueur[4])
                                                       )
        return self.ronde.utiliser_tableau_ronde()

    def recuperer_ronde_arbre(self):
        self.ronde.creer_arbre_ronde()
        for id_match in range(len(self.ronde.ronde_liste)):
            self.match.creer_arbre_match(self.ronde.arbre_ronde, id_match)
            self.match.utiliser_arbre_match().add(f'{self.ronde.ronde_liste[id_match][0][1]}')
            self.match.utiliser_arbre_match().add(f'{self.ronde.ronde_liste[id_match][1][1]}')
        return self.ronde.utiliser_arbre_ronde()

    def recuperer_match_arbre(self):
        for id_match in range(len(self.ronde.ronde_liste)):
            self.vue.afficher_joueur_remporte_match()
            self.vue.afficher_match_arbre(
                self.match.cree_arbre_resultat_match(self.ronde.ronde_liste, id_match))

            joueur_resultat = self.vue.entrer_resultat_match()

            if joueur_resultat == 1:
                self.ronde.ronde_liste[id_match][0][3].append(self.match.resultat_match[0])
                self.ronde.ronde_liste[id_match][1][3].append(self.match.resultat_match[1])

            elif joueur_resultat == 2:
                self.ronde.ronde_liste[id_match][0][3].append(self.match.resultat_match[1])
                self.ronde.ronde_liste[id_match][1][3].append(self.match.resultat_match[0])

            else:
                self.ronde.ronde_liste[id_match][0][3].append(self.match.resultat_match[2])
                self.ronde.ronde_liste[id_match][1][3].append(self.match.resultat_match[2])

    def trier_joueurs_tournoi_victoire(self) -> [list]:
        """Trie les joueurs d'un tournoi par victoire"""
        joueur_tournoi_trier = []
        for match in self.ronde.ronde_liste:
            for joueur in match:
                joueur_tournoi_trier.append([joueur[0], joueur[1], joueur[2], joueur[3], sum(joueur[3])])
        self.ronde.ronde_liste.clear()
        self.ronde.ronde_liste = sorted(joueur_tournoi_trier, key=itemgetter(4, 2), reverse=True)
        return self.ronde.ronde_liste

    def trier_joueurs_tournoi_classement(self) -> [list]:
        """Trie les joueurs d'un tournoi par classement"""
        joueur_tournoi_trier = []
        for id_joueur in self.tournoi.joueurs_tournoi:
            joueur_tournoi_trier.append([
                id_joueur,
                self.joueur.dict_joueurs[id_joueur][NOM],
                self.joueur.dict_joueurs[id_joueur][CLASSEMENT],
                []
            ])
        self.tournoi.joueurs_trier_classement = sorted(joueur_tournoi_trier, key=itemgetter(TRIE_CLASSEMENT),
                                                       reverse=True)
        return self.tournoi.joueurs_trier_classement

    def creer_premiere_ronde(self) -> [list]:
        """Creer la premiere ronde"""
        indice_joueur = (self.tournoi.joueurs_max / 2)
        self.ronde.joueurs_a = self.tournoi.joueurs_trier_classement[:int(indice_joueur)]
        self.ronde.joueurs_b = self.tournoi.joueurs_trier_classement[int(indice_joueur):]
        for joueur_a, joueur_b in zip(self.ronde.joueurs_a, self.ronde.joueurs_b):
            self.ronde.ronde_liste.append([joueur_a, joueur_b])
        return self.ronde.ronde_liste

    def creer_ronde(self) -> [list]:
        """Creer une ronde """
        self.ronde.joueurs_a.clear()
        self.ronde.joueurs_b.clear()
        for indice, joueur in enumerate(self.ronde.ronde_liste):
            if indice % 2 != 0:
                self.ronde.joueurs_a.append(joueur)
            else:
                self.ronde.joueurs_b.append(joueur)
        self.ronde.ronde_liste.clear()
        for joueur_a, joueur_b in zip(self.ronde.joueurs_a, self.ronde.joueurs_b):
            self.ronde.ronde_liste.append([joueur_a, joueur_b])
        return self.ronde.ronde_liste

    def ajouter_joueurs_tournoi(self) -> [list]:
        """"Ajouter des joueurs au tournoi"""
        self.vue.afficher_tournoi_tableau(self.recuperer_tournoi_tableau(NOM))
        self.tournoi.id_tournoi = self.vue.entrer_id()
        self.vue.effacer_ecran()
        self.vue.afficher_joueur_tableau(self.recuperer_joueur_tableau(CLASSEMENT, reverse=True))
        self.vue.afficher_ajouter_joueurs_tournoi()
        for competiteur in range(0, self.tournoi.joueurs_max):
            id_joueur = self.vue.entrer_id()
            self.tournoi.joueurs_tournoi.append(id_joueur)
        return self.tournoi.joueurs_tournoi

    def lancer_tournoi(self):
        """"Lancement du tournoi"""
        self.vue.effacer_ecran()
        self.vue.entrer_joueurs_tournoi_max()
        self.vue.entrer_rondes_tournoi_max()
        # Ajouter joueurs au tournoi choisi
        self.ajouter_joueurs_tournoi()
        self.tournoi.enregistrer_joueurs_tournoi(self.tournoi.id_tournoi)
        # trier les joueurs par classements
        self.trier_joueurs_tournoi_classement()
        self.creer_premiere_ronde()
        self.vue.afficher_ronde_arbre(self.recuperer_ronde_arbre())
        self.vue.afficher_match_arbre(self.recuperer_match_arbre())
        self.tournoi.enregistrer_ronde(self.tournoi.id_tournoi)
        self.trier_joueurs_tournoi_victoire()
        self.vue.afficher_ronde_tableau(self.recuperer_ronde_tableau())
        for nouvelle_ronde in range(1, self.tournoi.rondes_max):
            self.creer_ronde()
            self.vue.afficher_ronde_arbre(self.recuperer_ronde_arbre())
            self.vue.afficher_match_arbre(self.recuperer_match_arbre())
            self.tournoi.enregistrer_ronde(self.tournoi.id_tournoi)
            self.trier_joueurs_tournoi_victoire()
            self.vue.afficher_ronde_tableau(self.recuperer_ronde_tableau())
