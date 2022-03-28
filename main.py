from Modele import Joueur
from Modele import Match
from Modele import Ronde
from Modele import Tournoi
from Vue import Vue
from Vue import Menu
from Controleur import ControleMenu
from Controleur import Controleur

joueur = Joueur()
tournoi = Tournoi(Ronde())
vue = Vue(Menu())
programme = Controleur(vue, tournoi, joueur, Ronde(), Match())
menu = ControleMenu(vue, programme)

joueur.ajouter_joueur_dict(50, 'DUPONT', 'Nicolas', '05-07-1994', 'Masculin', 21)
joueur.ajouter_joueur_dict(51, 'DURAND', 'Martine', '21-05-1997', 'Féminin', 18)
joueur.ajouter_joueur_dict(52, 'BLANC', 'Camille', '09-11-1992', 'Féminin', 66)
joueur.ajouter_joueur_dict(53, 'BERNARD', 'Elise', '31-03-1976', 'Féminin', 41)
joueur.ajouter_joueur_dict(54, 'BERGER', 'Robert', '05-07-1986', 'Masculin', 39)
joueur.ajouter_joueur_dict(55, 'GIRARD', 'Lou', '05-07-2001', 'Masculin', 28)
joueur.ajouter_joueur_dict(56, 'DELORME', 'Margot', '05-07-2004', 'Masculin', 12)
joueur.ajouter_joueur_dict(57, 'FOURNIER', 'Damien', '05-07-1989', 'Masculin', 29)

tournoi.ajouter_tournoi_dict(31, 'CHESSMASTER', 'NANTES', '05-03-2022', 'Blitz', 'Super tournoi')
tournoi.ajouter_tournoi_dict(47, 'SUPERCHESS', 'PARIS', '05-07-2023', 'Coup Rapide', 'Super récompense')


if __name__ == "__main__":
    while True:
        menu.executer()


