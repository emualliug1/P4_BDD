# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from rich.panel import Panel
#############################################

# Définition des constantes

CONTINUER = '\nAppuyer sur entrer pour continuer'
MODIFICATION_ANNULE = '\nModification annulé'
JOUEUR_REMPORTE_MATCH = 'Quel joueur remporte le match ?'
JOUEUR_NOM = 'Nom de famille du joueur: '
JOUEUR_PRENOM = 'Prenom du joueur: '
JOUEUR_SEXE = '[0] = Masculin || [1] = Féminin: '
JOUEUR_DATE_NAISSANCE = 'Date de naissance JJ-MM-AAAA: '
JOUEUR_CLASSEMENT = 'Classement du joueur: '
TOURNOI_NOM = 'Nom du Tournoi: '
TOURNOI_LIEU = 'Lieu du Tournoi: '
TOURNOI_DATE = 'Date du tournoi JJ-MM-AAAA: '
TOURNOI_CONTROLE_TEMPS = '[0] = Bullet || [1] = Blitz || [2] = Coup rapide :'
TOURNOI_DESCRIPTION = 'Description du Tournoi: '
CHOISIR_NOMBRES_JOUEURS = 'Choisir un nombre de joueurs maximum pour le tournoi: '
CHOISIR_NOMBRES_RONDES = 'Choisir le nombre de ronde maximum pour le tournoi: '
ADMIN_CHOIX_ID = 'Choisir un ID: '
ADMIN_VALIDATION = 'Voulez vous modifier les informations [blue]o[/blue] ou [red]n[/red]: '
DATE_TOURNOI = 'Date du tournoi'
JOUEUR_GAGNANT = '\n[1] Joueur 1 || [2] Joueur 2 || [3] Match Nul: '
AJOUTER_JOUEURS_TOURNOI = '\nAjouter 8 ID de joueurs au tournoi: '
VAINQUEUR = 'Le gagnant du tournoi est: '

# Définition de la classe


class Vue(Console):
    """Affiche les informations du tournoi dans la console"""

    def __init__(self, vue):
        Console.__init__(self)
        self.vue = vue
        self.entrer_str = Prompt
        self.entrer_int = IntPrompt

    @staticmethod
    def effacer_ecran():
        """Efface l'écran de la console"""
        os.system('cls')

    def pause_ecran(self) -> [None]:
        """Met l'écran en pause dans la console"""
        self.afficher_continuer()
        input()

# Gérer Menu

    def afficher_menu_global(self):
        return self.vue.menu_global()

    def afficher_menu_tournoi(self):
        return self.vue.menu_tournoi()

    def afficher_menu_joueur(self):
        return self.vue.menu_joueur()

    def afficher_menu_rapport(self):
        return self.vue.menu_rapport()

    def afficher_menu_rapport_liste_joueurs(self):
        return self.vue.menu_rapport_liste_joueurs()

    def afficher_menu_rapport_liste_joueurs_tournoi(self):
        return self.vue.menu_rapport_liste_joueurs_tournoi()

    def entrer_choix_menu(self) -> [int]:
        """Entrer un choix pour naviguer dans le menu"""
        option = self.entrer_int.ask()
        return option

# Print

    def afficher_continuer(self):
        self.print(Panel.fit(CONTINUER))

    def afficher_modification_annule(self):
        self.print(Panel.fit(MODIFICATION_ANNULE))

    def afficher_joueur_remporte_match(self):
        self.print(Panel.fit(JOUEUR_REMPORTE_MATCH))

    def afficher_ajouter_joueurs_tournoi(self):
        self.print(Panel.fit(AJOUTER_JOUEURS_TOURNOI))

    def afficher_vainqueur_tournoi(self, joueur_gagnant):
        self.effacer_ecran()
        self.print(Panel.fit(f'{VAINQUEUR}{joueur_gagnant}'))
        self.pause_ecran()

# Tableau

    def afficher_joueur_tableau(self, tableau):
        """Affiche les joueurs enregistrés par classement"""
        self.effacer_ecran()
        self.print(tableau)
        self.pause_ecran()

    def afficher_tournoi_tableau(self, tableau):
        """Affiche les informations des tournois enregistrés"""
        self.effacer_ecran()
        self.print(tableau)
        self.pause_ecran()

    def afficher_ronde_tableau(self, tableau):
        """Affiche le resultat des rondes"""
        self.effacer_ecran()
        self.print(tableau)
        self.pause_ecran()

    def afficher_match_tableau(self, tableau):
        """Affiche le resultat d'un match sous forme d'un tableau"""
        self.effacer_ecran()
        self.print(tableau)
        self.pause_ecran()

    def afficher_joueurs_tournoi_tableau(self, tableau):
        """Afficher les joueurs d'un tournoi"""
        self.effacer_ecran()
        self.print(tableau)
        self.pause_ecran()

    def afficher_ronde_match_tournoi_tableau(self, tableau):
        """Affiche les rondes et les matchs d'un tournoi"""
        self.print(tableau)
# Arbre

    def afficher_ronde_arbre(self, arbre):
        """Affiche une ronde"""
        self.effacer_ecran()
        self.print(arbre)
        self.pause_ecran()

    def afficher_match_arbre(self, arbre):
        """Affiche le resultat d'un match sous forme d'un arbre"""
        self.effacer_ecran()
        self.print(arbre)

# Input

    def entrer_nom_joueur(self) -> [str]:
        """Entrer le nom d'un joueur"""
        nom_joueur = self.entrer_str.ask(JOUEUR_NOM)
        return nom_joueur

    def entrer_prenom_joueur(self) -> [str]:
        """Entrer le prenom d'un joueur"""
        prenom_joueur = self.entrer_str.ask(JOUEUR_PRENOM)
        return prenom_joueur

    def entrer_sexe_joueur(self) -> [int]:
        """Entrer le sexe d'un joueur"""
        sexe_joueur = self.entrer_int.ask(JOUEUR_SEXE)
        return sexe_joueur

    def entrer_date_naissance_joueur(self) -> [str]:
        """Entrer la data de naissance d'un joueur"""
        date_naissance_joueur = self.entrer_str.ask(JOUEUR_DATE_NAISSANCE)
        return date_naissance_joueur

    def entrer_classement_joueur(self) -> [int]:
        """Entrer le classement d'un joueur"""
        classement_joueur = self.entrer_int.ask(JOUEUR_CLASSEMENT)
        return classement_joueur

    def entrer_nom_tournoi(self) -> [str]:
        """Entrer le nom d'un tournoi"""
        nom_tournoi = self.entrer_str.ask(TOURNOI_NOM)
        return nom_tournoi

    def entrer_lieu_tournoi(self) -> [str]:
        """Entrer le lieu d'un tournoi"""
        lieu_tournoi = self.entrer_str.ask(TOURNOI_LIEU)
        return lieu_tournoi

    def entrer_date_tournoi(self) -> [str]:
        """Entrer une date pour un tournoi"""
        date_tournoi = self.entrer_str.ask(TOURNOI_DATE)
        return date_tournoi

    def entrer_controle_temps_tournoi(self) -> [int]:
        """Entrer le type de tournoi"""
        controle_temps = self.entrer_int.ask(TOURNOI_CONTROLE_TEMPS)
        return controle_temps

    def entrer_description_tournoi(self) -> [str]:
        """Entrer une description pour un tournoi"""
        description = self.entrer_str.ask(TOURNOI_DESCRIPTION)
        return description

    def entrer_id(self) -> [int]:
        """Entrer une ID"""
        id_validation = self.entrer_int.ask(ADMIN_CHOIX_ID)
        return id_validation

    def entrer_validation(self) -> [int]:
        """Entrer une validation"""
        validation = self.entrer_str.ask(ADMIN_VALIDATION)
        if validation == "n":
            return False
        return True

    def entrer_resultat_match(self) -> [int]:
        """Entrer le resultat d'un match"""
        joueur_resultat = self.entrer_int.ask(JOUEUR_GAGNANT)
        return joueur_resultat

    def entrer_joueurs_tournoi_max(self) -> [int]:
        """Entrer le nombre de joueurs maximum d'un tournoi"""
        joueurs_max = self.entrer_str.ask(CHOISIR_NOMBRES_JOUEURS)
        return joueurs_max

    def entrer_rondes_tournoi_max(self) -> [int]:
        """Entrer le nombre de rondes maximum d'un tournoi"""
        rondes_max = self.entrer_int.ask(CHOISIR_NOMBRES_RONDES)
        return rondes_max
