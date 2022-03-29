# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from Modele import Joueur
from Modele import Match
from Modele import Ronde
from Modele import Tournoi
from Modele import Modele
from Vue import Vue
from Vue import Menu
from Controleur import ControleMenu
from Controleur import Controleur
#############################################

# Définition des classes du programme

vue = Vue(Menu())
modele = Modele(Tournoi(), Joueur(), Match(), Ronde())
programme = Controleur(vue, modele)
menu = ControleMenu(vue, programme)


if __name__ == "__main__":
    while True:
        menu.executer()
