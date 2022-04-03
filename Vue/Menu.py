# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from rich.console import Console
#############################################

# Définition de la classe


class Menu(Console):
    def __init__(self):
        Console.__init__(self)

    def menu_global(self):
        self.print('[1] Tournois')
        self.print('[2] Joueurs')
        self.print('[3] Rapports')
        self.print('[4] Quitter')

    def menu_tournoi(self):
        self.print('[1] Ajouter un tournoi')
        self.print('[2] Modifier un tournoi')
        self.print('[3] Lancer Tournoi')
        self.print('[4] Retour')

    def menu_joueur(self):
        self.print('[1] Ajouter un joueur')
        self.print('[2] Modifier un joueur')
        self.print('[3] Retour')

    def menu_rapport(self):
        self.print('[1] Liste de tous les joueurs')
        self.print("[2] Liste de tous les joueurs d'un tournoi")
        self.print('[3] Liste de tous les tournois')
        self.print("[4] Liste des rondes et des match d'un tournoi")
        self.print("[5] Retour")

    def menu_rapport_liste_joueurs(self):
        self.print('[1] Liste de tous les joueurs par ordre alphabétique')
        self.print('[2] Liste de tous les joueurs par classement')
        self.print('[3] Retour')

    def menu_rapport_liste_joueurs_tournoi(self):
        self.print('[1] Liste de tous les joueurs du tournoi par ordre alphabétique')
        self.print('[2] Liste de tous les joueurs du tournoi par classement')
        self.print('[3] Retour')
