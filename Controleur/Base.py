# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
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
JOUEURS_TOURNOI = 'Joueurs du tournoi'
JOUEURS = 'Joueurs'

# Définition de la classe


class Controleur:

    def __init__(self, vue, modele):
        self.vue = vue
        self.modele = modele

    def recuperer_information_joueur(self):
        self.vue.effacer_ecran()
        self.modele.joueur.nom_famille = self.vue.entrer_nom_joueur()
        self.modele.joueur.prenom = self.vue.entrer_prenom_joueur()
        self.modele.joueur.date_naissance = self.vue.entrer_date_naissance_joueur()
        self.modele.joueur.sexe = self.vue.entrer_sexe_joueur()
        self.modele.joueur.classement = self.vue.entrer_classement_joueur()

    def recuperer_information_tournoi(self):
        self.vue.effacer_ecran()
        self.modele.tournoi.nom_tournoi = self.vue.entrer_nom_tournoi()
        self.modele.tournoi.lieu = self.vue.entrer_lieu_tournoi()
        self.modele.tournoi.date_tournoi = self.vue.entrer_date_tournoi()
        self.modele.tournoi.controle_temps = self.vue.entrer_controle_temps_tournoi()
        self.modele.tournoi.description = self.vue.entrer_description_tournoi()

    def modifier_joueur(self):
        """"Modification d'un joueur"""
        self.vue.effacer_ecran()
        self.vue.afficher_joueur_tableau(self.recuperer_joueur_tableau(NOM))
        joueur_id = self.vue.entrer_id()
        validation = self.vue.entrer_validation()
        if validation:
            self.recuperer_information_joueur()
            self.modele.joueur.enregistrer_joueur(joueur_id)
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
            self.modele.enregistrer_db_tournoi_modifier(tournoi_id)
        if not validation:
            self.vue.afficher_modification_annule()
            self.vue.pause_ecran()

    @staticmethod
    def trier_table(table, trie, reverse=False):
        table_trier = (sorted(table, key=itemgetter(trie), reverse=reverse))
        return table_trier

    def recuperer_joueur_tableau(self, trie, reverse=False):
        self.modele.joueur.creer_tableau_joueur()
        for joueur in self.trier_table(self.modele.db_joueur_table, trie, reverse):
            self.modele.joueur.utiliser_tableau_joueur().add_row(str(joueur.doc_id),
                                                          joueur[NOM],
                                                          joueur[PRENOM],
                                                          joueur[DATE_NAISSANCE],
                                                          joueur[SEXE],
                                                          str(joueur[CLASSEMENT]))
        return self.modele.joueur.utiliser_tableau_joueur()

    def recuperer_tournoi_tableau(self, trie):
        self.modele.tournoi.creer_tableau_tournoi()
        for tournoi in self.trier_table(self.modele.db_tournoi_table, trie):
            self.modele.tournoi.utiliser_tableau_tournoi().add_row(str(tournoi.doc_id),
                                                            tournoi[NOM],
                                                            tournoi[LIEU],
                                                            tournoi[CONTROLE_TEMPS],
                                                            tournoi[DATE_TOURNOI],
                                                            tournoi[DESCRIPTION])
        return self.modele.tournoi.utiliser_tableau_tournoi()

    def recuperer_ronde_tableau(self):
        self.modele.ronde.creer_tableau_ronde()
        for joueur in self.modele.ronde.ronde_liste:
            self.modele.ronde.utiliser_tableau_ronde().add_row(
                                                        str(joueur[0]),
                                                        str(joueur[1]),
                                                        str(joueur[2]),
                                                        str(joueur[3]),
                                                        str(joueur[4])
                                                       )
        return self.modele.ronde.utiliser_tableau_ronde()

    def recuperer_ronde_arbre(self):
        self.modele.ronde.creer_arbre_ronde()
        for id_match in range(len(self.modele.ronde.ronde_liste)):
            self.modele.match.creer_arbre_match(self.modele.ronde.arbre_ronde, id_match)
            self.modele.match.utiliser_arbre_match().add(f'{self.modele.ronde.ronde_liste[id_match][0][1]}')
            self.modele.match.utiliser_arbre_match().add(f'{self.modele.ronde.ronde_liste[id_match][1][1]}')
        return self.modele.ronde.utiliser_arbre_ronde()

    def recuperer_match_arbre(self):
        for id_match in range(len(self.modele.ronde.ronde_liste)):
            self.vue.afficher_joueur_remporte_match()
            self.vue.afficher_match_arbre(
                self.modele.match.cree_arbre_resultat_match(self.modele.ronde.ronde_liste, id_match))

            joueur_resultat = self.vue.entrer_resultat_match()

            if joueur_resultat == 1:
                self.modele.ronde.ronde_liste[id_match][0][3].append(self.modele.match.resultat_match[0])
                self.modele.ronde.ronde_liste[id_match][1][3].append(self.modele.match.resultat_match[1])

            elif joueur_resultat == 2:
                self.modele.ronde.ronde_liste[id_match][0][3].append(self.modele.match.resultat_match[1])
                self.modele.ronde.ronde_liste[id_match][1][3].append(self.modele.match.resultat_match[0])

            else:
                self.modele.ronde.ronde_liste[id_match][0][3].append(self.modele.match.resultat_match[2])
                self.modele.ronde.ronde_liste[id_match][1][3].append(self.modele.match.resultat_match[2])

    def trier_joueurs_tournoi_victoire(self) -> [list]:
        """Trie les joueurs d'un tournoi par victoire"""
        joueur_tournoi_trier = []
        for match in self.modele.ronde.ronde_liste:
            for joueur in match:
                joueur_tournoi_trier.append([joueur[0], joueur[1], joueur[2], joueur[3], sum(joueur[3])])
        self.modele.ronde.ronde_liste.clear()
        self.modele.ronde.ronde_liste = sorted(joueur_tournoi_trier, key=itemgetter(4, 2), reverse=True)
        return self.modele.ronde.ronde_liste

    def trier_joueurs_tournoi_classement(self) -> [list]:
        """Trie les joueurs d'un tournoi par classement"""
        joueur_tournoi_trier = []
        for id_joueur in self.modele.tournoi.joueurs_tournoi:
            joueur_tournoi_trier.append([
                id_joueur,
                self.modele.joueur.dict_joueurs[id_joueur][NOM],
                self.modele.joueur.dict_joueurs[id_joueur][CLASSEMENT],
                []
            ])
        self.modele.tournoi.joueurs_trier_classement = sorted(joueur_tournoi_trier, key=itemgetter(TRIE_CLASSEMENT),
                                                       reverse=True)
        return self.modele.tournoi.joueurs_trier_classement

    def creer_premiere_ronde(self) -> [list]:
        """Creer la premiere ronde"""
        indice_joueur = (self.modele.tournoi.joueurs_max / 2)
        self.modele.ronde.joueurs_a = self.modele.tournoi.joueurs_trier_classement[:int(indice_joueur)]
        self.modele.ronde.joueurs_b = self.modele.tournoi.joueurs_trier_classement[int(indice_joueur):]
        for joueur_a, joueur_b in zip(self.modele.ronde.joueurs_a, self.modele.ronde.joueurs_b):
            self.modele.ronde.ronde_liste.append([joueur_a, joueur_b])
        return self.modele.ronde.ronde_liste

    def creer_ronde(self) -> [list]:
        """Creer une ronde """
        self.modele.ronde.joueurs_a.clear()
        self.modele.ronde.joueurs_b.clear()
        for indice, joueur in enumerate(self.modele.ronde.ronde_liste):
            if indice % 2 != 0:
                self.modele.ronde.joueurs_a.append(joueur)
            else:
                self.modele.ronde.joueurs_b.append(joueur)
        self.modele.ronde.ronde_liste.clear()
        for joueur_a, joueur_b in zip(self.modele.ronde.joueurs_a, self.modele.ronde.joueurs_b):
            self.modele.ronde.ronde_liste.append([joueur_a, joueur_b])
        return self.modele.ronde.ronde_liste

    def ajouter_joueurs_tournoi(self) -> [list]:
        """"Ajouter des joueurs au tournoi"""
        self.vue.afficher_tournoi_tableau(self.recuperer_tournoi_tableau(NOM))
        self.modele.tournoi.id_tournoi = self.vue.entrer_id()
        self.vue.effacer_ecran()
        self.vue.afficher_joueur_tableau(self.recuperer_joueur_tableau(CLASSEMENT, reverse=True))
        self.vue.afficher_ajouter_joueurs_tournoi()
        for competiteur in range(0, self.modele.tournoi.joueurs_max):
            id_joueur = self.vue.entrer_id()
            self.modele.tournoi.joueurs_tournoi.append(id_joueur)
        return self.modele.tournoi.joueurs_tournoi



    def lancer_tournoi(self):
        """"Lancement du tournoi"""
        self.vue.effacer_ecran()
        self.vue.entrer_joueurs_tournoi_max()
        self.vue.entrer_rondes_tournoi_max()
        # Ajouter joueurs au tournoi choisi
        self.ajouter_joueurs_tournoi()
        self.modele.enregistrer_db_tournoi_joueurs(self.modele.tournoi.id_tournoi)
        # trier les joueurs par classements
        self.trier_joueurs_tournoi_classement()
        self.creer_premiere_ronde()
        self.vue.afficher_ronde_arbre(self.recuperer_ronde_arbre())
        self.vue.afficher_match_arbre(self.recuperer_match_arbre())
        self.modele.tournoi.enregistrer_ronde(self.modele.tournoi.id_tournoi)
        self.trier_joueurs_tournoi_victoire()
        self.vue.afficher_ronde_tableau(self.recuperer_ronde_tableau())
        for nouvelle_ronde in range(1, self.modele.tournoi.rondes_max):
            self.creer_ronde()
            self.vue.afficher_ronde_arbre(self.recuperer_ronde_arbre())
            self.vue.afficher_match_arbre(self.recuperer_match_arbre())
            self.modele.tournoi.enregistrer_ronde(self.modele.tournoi.id_tournoi)
            self.trier_joueurs_tournoi_victoire()
            self.vue.afficher_ronde_tableau(self.recuperer_ronde_tableau())
