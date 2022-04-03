# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from operator import itemgetter
from rich.table import Table
from rich.tree import Tree
from tinydb import TinyDB
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
RONDE = 'Ronde'
GAGNER = 1
PERDU = 2
NUL = 3
MATCH_GAGNER = 1
MATCH_PERDU = 0
MATCH_NUL = 2
MATCH_NUL_ = 0.5
JOUEUR_A = 0
JOUEUR_B = 1
JOUEUR_NOM = 3
SCORE_TOURNOI = 4
CLASSEMENT_JOUEUR = 2
RONDE_ID_JOUEUR = 0
RONDE_NOM_JOUEUR = 1
RONDE_CLASSEMENT_JOUEUR = 2
RONDE_SCORES_MATCH_JOUEUR = 3
RONDE_TOTAL_SCORE_JOUEUR = 4
PAIRE = 2
IMPAIRE = 0
DEBUT = 0
DEBUT_RONDE = 1
AJOUTER_RONDE = 1
COMPTEUR = 1
AUCUN_GAGNANT = 'Match Nul'
MATCH = 'Match'

# Définition de la classe


class Controleur:

    def __init__(self, vue, modele):
        self.vue = vue
        self.modele = modele

    def recuperer_information_joueur(self):
        """Récupère les informations d'un joueur"""
        self.vue.effacer_ecran()
        self.modele.joueur.nom_famille = self.vue.entrer_nom_joueur()
        self.modele.joueur.prenom = self.vue.entrer_prenom_joueur()
        self.modele.joueur.date_naissance = self.vue.entrer_date_naissance_joueur()
        self.modele.joueur.sexe = self.vue.entrer_sexe_joueur()
        self.modele.joueur.classement = self.vue.entrer_classement_joueur()

    def recuperer_information_tournoi(self):
        """Récupère les informations d'un tournoi"""
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
            self.modele.enregistrer_db_joueur_modifier(joueur_id)
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

    def recuperer_joueurs_tournoi(self, trie, reverse=False) -> [Table]:
        """Récupérer les joueurs d'un tournoi (menu rapport)"""
        self.vue.effacer_ecran()
        self.vue.afficher_tournoi_tableau(self.recuperer_tournoi_tableau(NOM))
        tournoi_id = self.vue.entrer_id()
        self.modele.tournoi.creer_tableau_joueurs_tournoi()
        for tournoi in self.modele.db_tournoi_table:
            if tournoi_id == tournoi.doc_id:
                for joueur in self.trier_table(self.modele.db_joueur_table, trie, reverse):
                    for joueur_du_tournoi in tournoi[JOUEURS_TOURNOI]:
                        if joueur.doc_id == joueur_du_tournoi:
                            self.modele.tournoi.utiliser_tableau_joueurs_tournoi().add_row(
                                str(joueur_du_tournoi),
                                str(joueur[NOM]),
                                str(joueur[CLASSEMENT]))
        return self.modele.tournoi.utiliser_tableau_joueurs_tournoi()

    def recuperer_ronde_match_tournoi(self):
        """Récupérer les rondes du tournoi (menu rapport)"""
        score = -1
        self.vue.afficher_tournoi_tableau(self.recuperer_tournoi_tableau(NOM))
        tournoi_id = self.vue.entrer_id()
        tournoi = self.modele.db_tournoi_table.get(doc_id=tournoi_id)
        for id_ronde in range(DEBUT_RONDE, self.modele.tournoi.rondes_max + AJOUTER_RONDE):
            id_match = DEBUT
            score += COMPTEUR
            self.modele.match.cree_tableau_ronde_match_tournoi(f'{RONDE}{id_ronde}')
            for match in tournoi[f'{RONDE}{id_ronde}']:
                for resultat in range(score, len(match[JOUEUR_A][RONDE_SCORES_MATCH_JOUEUR])):
                    id_match += COMPTEUR
                    score_match = match[JOUEUR_A][RONDE_SCORES_MATCH_JOUEUR][score]
                    if score_match == MATCH_PERDU:
                        self.modele.match.utiliser_tableau_ronde_match_tournoi().add_row(
                            str(f'{MATCH}{id_match}'),
                            match[JOUEUR_A][RONDE_NOM_JOUEUR],
                            match[JOUEUR_B][RONDE_NOM_JOUEUR],
                            match[JOUEUR_B][RONDE_NOM_JOUEUR])
                    elif score_match == MATCH_GAGNER:
                        self.modele.match.utiliser_tableau_ronde_match_tournoi().add_row(
                            str(f'{MATCH}{id_match}'),
                            match[JOUEUR_A][RONDE_NOM_JOUEUR],
                            match[JOUEUR_B][RONDE_NOM_JOUEUR],
                            match[JOUEUR_A][RONDE_NOM_JOUEUR])
                    elif score_match == MATCH_NUL_:
                        self.modele.match.utiliser_tableau_ronde_match_tournoi().add_row(
                            str(f'{MATCH}{id_match}'),
                            match[JOUEUR_A][RONDE_NOM_JOUEUR],
                            match[JOUEUR_B][RONDE_NOM_JOUEUR],
                            AUCUN_GAGNANT)

        return self.modele.match.utiliser_tableau_ronde_match_tournoi()

    @staticmethod
    def trier_table(table, trie, reverse=False) -> [TinyDB.table]:
        """Permet le trie par (NOM, CLASSEMENT) d'une table de la BDD """
        table_trier = (sorted(table, key=itemgetter(trie), reverse=reverse))
        return table_trier

    def recuperer_joueur_tableau(self, trie, reverse=False) -> [Table]:
        """Récupère les informations des joueurs dans la BDD """
        self.modele.joueur.creer_tableau_joueur()
        for joueur in self.trier_table(self.modele.db_joueur_table, trie, reverse):
            self.modele.joueur.utiliser_tableau_joueur().add_row(
                str(joueur.doc_id),
                joueur[NOM],
                joueur[PRENOM],
                joueur[DATE_NAISSANCE],
                joueur[SEXE],
                str(joueur[CLASSEMENT]))
        return self.modele.joueur.utiliser_tableau_joueur()

    def recuperer_tournoi_tableau(self, trie) -> [Table]:
        """"Récupère les informations des tournois dans la BDD"""
        self.modele.tournoi.creer_tableau_tournoi()
        for tournoi in self.trier_table(self.modele.db_tournoi_table, trie):
            self.modele.tournoi.utiliser_tableau_tournoi().add_row(
                str(tournoi.doc_id),
                tournoi[NOM],
                tournoi[LIEU],
                tournoi[CONTROLE_TEMPS],
                tournoi[DATE_TOURNOI],
                tournoi[DESCRIPTION])
        return self.modele.tournoi.utiliser_tableau_tournoi()

    def recuperer_ronde_tableau(self) -> [Table]:
        """Récupère les informations d'une ronde pour un affichage en mode tableau"""
        self.modele.ronde.creer_tableau_ronde()
        for joueur in self.modele.ronde.ronde_liste:
            self.modele.ronde.utiliser_tableau_ronde().add_row(
                str(joueur[RONDE_ID_JOUEUR]),
                str(joueur[RONDE_NOM_JOUEUR]),
                str(joueur[RONDE_CLASSEMENT_JOUEUR]),
                str(joueur[RONDE_SCORES_MATCH_JOUEUR]),
                str(joueur[RONDE_TOTAL_SCORE_JOUEUR])
            )
        return self.modele.ronde.utiliser_tableau_ronde()

    def recuperer_ronde_arbre(self) -> [Tree]:
        """Récupère les informations d'une ronde pour affichage en mode arbre"""
        self.modele.ronde.creer_arbre_ronde()
        for id_match in range(len(self.modele.ronde.ronde_liste)):
            self.modele.match.creer_arbre_match(self.modele.ronde.arbre_ronde, id_match)
            self.modele.match.utiliser_arbre_match().add(
                f'{self.modele.ronde.ronde_liste[id_match][JOUEUR_A][RONDE_NOM_JOUEUR]}')
            self.modele.match.utiliser_arbre_match().add(
                f'{self.modele.ronde.ronde_liste[id_match][JOUEUR_B][RONDE_NOM_JOUEUR]}')
        return self.modele.ronde.utiliser_arbre_ronde()

    def recuperer_match_arbre(self):
        """Récupère les informations d'un match pour un affichage en mode arbre"""
        for id_match in range(len(self.modele.ronde.ronde_liste)):
            self.vue.afficher_match_arbre(
                self.modele.match.cree_arbre_resultat_match(
                    self.modele.ronde.ronde_liste, id_match))
            self.vue.afficher_joueur_remporte_match()
            joueur_resultat = self.vue.entrer_resultat_match()

            if joueur_resultat == GAGNER:
                self.modele.ronde.ronde_liste[id_match][JOUEUR_A][JOUEUR_NOM].append(
                    self.modele.match.resultat_match[MATCH_GAGNER])
                self.modele.ronde.ronde_liste[id_match][JOUEUR_B][JOUEUR_NOM].append(
                    self.modele.match.resultat_match[MATCH_PERDU])

            elif joueur_resultat == PERDU:
                self.modele.ronde.ronde_liste[id_match][JOUEUR_A][JOUEUR_NOM].append(
                    self.modele.match.resultat_match[MATCH_PERDU])
                self.modele.ronde.ronde_liste[id_match][JOUEUR_B][JOUEUR_NOM].append(
                    self.modele.match.resultat_match[MATCH_GAGNER])

            elif joueur_resultat == NUL:
                self.modele.ronde.ronde_liste[id_match][JOUEUR_A][JOUEUR_NOM].append(
                    self.modele.match.resultat_match[MATCH_NUL])
                self.modele.ronde.ronde_liste[id_match][JOUEUR_B][JOUEUR_NOM].append(
                    self.modele.match.resultat_match[MATCH_NUL])

    def trier_joueurs_tournoi_victoire(self) -> [list]:
        """Trie les joueurs d'un tournoi par victoire"""
        joueur_tournoi_trier = []
        for match in self.modele.ronde.ronde_liste:
            for joueur in match:
                joueur_tournoi_trier.append(
                    [joueur[RONDE_ID_JOUEUR],
                     joueur[RONDE_NOM_JOUEUR],
                     joueur[RONDE_CLASSEMENT_JOUEUR],
                     joueur[RONDE_SCORES_MATCH_JOUEUR],
                     sum(joueur[RONDE_SCORES_MATCH_JOUEUR])])
        self.modele.ronde.ronde_liste.clear()
        self.modele.ronde.ronde_liste = sorted(joueur_tournoi_trier, key=itemgetter(
            SCORE_TOURNOI, CLASSEMENT_JOUEUR), reverse=True)
        return self.modele.ronde.ronde_liste

    def trier_joueurs_tournoi_classement(self) -> [list]:
        """Trie les joueurs d'un tournoi par classement"""
        joueur_tournoi_trier = []
        for id_joueur in self.modele.tournoi.joueurs_tournoi:
            for joueur in self.modele.db_joueur_table:
                if id_joueur == joueur.doc_id:
                    joueur_tournoi_trier.append([
                        id_joueur,
                        joueur[NOM],
                        joueur[CLASSEMENT],
                        []
                    ])
        self.modele.tournoi.joueurs_trier_classement = sorted(
            joueur_tournoi_trier, key=itemgetter(TRIE_CLASSEMENT), reverse=True)
        return self.modele.tournoi.joueurs_trier_classement

    def creer_premiere_ronde(self) -> [list]:
        """Creer la premiere ronde"""
        indice_joueur = (self.modele.tournoi.joueurs_max / PAIRE)
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
            if indice % PAIRE != IMPAIRE:
                self.modele.ronde.joueurs_a.append(joueur)
            else:
                self.modele.ronde.joueurs_b.append(joueur)
        self.modele.ronde.ronde_liste.clear()
        for joueur_a, joueur_b in zip(self.modele.ronde.joueurs_a, self.modele.ronde.joueurs_b):
            self.modele.ronde.ronde_liste.append([joueur_a, joueur_b])
        return self.modele.ronde.ronde_liste

    def ajouter_joueurs_tournoi(self) -> [list]:
        """"Ajouter des joueurs au tournoi"""
        self.vue.effacer_ecran()
        self.vue.afficher_tournoi_tableau(self.recuperer_tournoi_tableau(NOM))
        self.modele.tournoi.id_tournoi = self.vue.entrer_id()
        self.vue.entrer_joueurs_tournoi_max()
        self.modele.enregistrer_db_tournoi_joueur_max(self.modele.tournoi.id_tournoi)
        self.vue.entrer_rondes_tournoi_max()
        self.modele.enregistrer_db_tournoi_ronde_max(self.modele.tournoi.id_tournoi)
        self.vue.effacer_ecran()
        self.vue.afficher_joueur_tableau(self.recuperer_joueur_tableau(CLASSEMENT, reverse=True))
        self.vue.afficher_ajouter_joueurs_tournoi()
        for competiteur in range(DEBUT, self.modele.tournoi.joueurs_max):
            id_joueur = self.vue.entrer_id()
            self.modele.tournoi.joueurs_tournoi.append(id_joueur)
        return self.modele.tournoi.joueurs_tournoi

    def lancer_tournoi(self):
        """"Lancement du tournoi"""
        self.ajouter_joueurs_tournoi()
        self.modele.enregistrer_db_tournoi_joueurs(self.modele.tournoi.id_tournoi)
        self.trier_joueurs_tournoi_classement()
        self.creer_premiere_ronde()
        self.vue.afficher_ronde_arbre(self.recuperer_ronde_arbre())
        self.recuperer_match_arbre()
        self.modele.enregistrer_db_tournoi_ronde(self.modele.tournoi.id_tournoi)
        self.trier_joueurs_tournoi_victoire()
        self.vue.afficher_ronde_tableau(self.recuperer_ronde_tableau())
        for nouvelle_ronde in range(DEBUT_RONDE, self.modele.tournoi.rondes_max):
            self.creer_ronde()
            self.vue.afficher_ronde_arbre(self.recuperer_ronde_arbre())
            self.recuperer_match_arbre()
            self.modele.enregistrer_db_tournoi_ronde(self.modele.tournoi.id_tournoi)
            self.trier_joueurs_tournoi_victoire()
            self.vue.afficher_ronde_tableau(self.recuperer_ronde_tableau())
        self.vue.afficher_vainqueur_tournoi(self.modele.ronde.recuperer_vainqueur_tournoi())
