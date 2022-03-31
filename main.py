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


def main():
    vue = Vue(Menu())
    modele = Modele(Tournoi(), Joueur(), Ronde(), Match())
    programme = Controleur(vue, modele)
    menu = ControleMenu(vue, programme)
    menu.executer()


if __name__ == "__main__":
    while True:
        main()
