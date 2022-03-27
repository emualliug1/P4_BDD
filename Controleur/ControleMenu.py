
# -----------------------------------------définition des constantes-------------------------------
# Constante de trie
NOM = 'Nom'
CLASSEMENT = 'Classement'

# Constante menu global
TOURNOI = 1
JOUEURS = 2
RAPPORTS = 3
QUITTER = 4

# Constante menu tournoi
AJOUTER_TOURNOI = 1
MODIFIER_TOURNOI = 2
LANCER_TOURNOI = 3
RETOUR_MENU_GLOBAL_1 = 4

# Constante menu joueur
AJOUTER_JOUEUR = 1
MODIFIER_JOUEUR = 2
RETOUR_MENU_GLOBAL_2 = 3

# Constante menu rapports
AFFICHER_JOUEURS = 1
AFFICHER_JOUEURS_TOURNOI = 2
AFFICHER_TOURNOIS = 3
AFFICHER_TOURS_TOURNOI = 4
AFFICHER_MATCH_TOURNOI = 5
RETOUR_MENU_GLOBAL_3 = 6

# Constante menu rapports joueur
AFFICHER_JOUEURS_ALPHA = 1
AFFICHER_JOUEURS_CLASSEMENT = 2
RETOUR_MENU_RAPPORTS_1 = 3

# Constante menu rapports joueur tournoi
AFFICHER_JOUEURS_TOURNOI_ALPHA = 1
AFFICHER_JOUEURS_TOURNOI_CLASSEMENT = 2
RETOUR_MENU_RAPPORTS_2 = 3

# -----------------------------------------définition de la classe---------------------------------


class ControleMenu:
    def __init__(self, vue, controle):
        self.vue = vue
        self.controle = controle

    def executer(self):
        self.choix_menu_global()

    def choix_menu_global(self):
        self.vue.effacer_ecran()
        self.vue.afficher_menu_global()
        option = self.vue.entrer_choix_menu()

        if option == TOURNOI:
            self.vue.effacer_ecran()
            self.vue.afficher_menu_tournoi()
            self.choix_menu_tournoi()
        elif option == JOUEURS:
            self.vue.effacer_ecran()
            self.vue.afficher_menu_joueur()
            self.choix_menu_joueur()
        elif option == RAPPORTS:
            self.vue.effacer_ecran()
            self.vue.afficher_menu_rapport()
            self.choix_menu_rapport()
        elif option == QUITTER:
            quit()


    def choix_menu_tournoi(self):
        option = self.vue.entrer_choix_menu()
        if option == AJOUTER_TOURNOI:
            self.vue.effacer_ecran()
            self.controle.recuperer_information_tournoi()
        elif option == MODIFIER_TOURNOI:
            pass
        elif option == LANCER_TOURNOI:
            pass
        elif option == RETOUR_MENU_GLOBAL_1:
            self.choix_menu_global()

    def choix_menu_joueur(self):
        option = self.vue.entrer_choix_menu()
        if option == AJOUTER_JOUEUR:
            self.vue.effacer_ecran()
            self.controle.recuperer_information_joueur()
        elif option == MODIFIER_JOUEUR:
            pass
        elif option == RETOUR_MENU_GLOBAL_2:
            self.choix_menu_global()

    def choix_menu_rapport(self):
        option = self.vue.entrer_choix_menu()
        if option == AFFICHER_JOUEURS:
            self.vue.effacer_ecran()
            self.vue.afficher_menu_rapport_liste_joueurs()
            self.choix_menu_rapport_liste_joueurs()
        elif option == AFFICHER_JOUEURS_TOURNOI:
            self.vue.effacer_ecran()
            self.vue.afficher_menu_rapport_liste_joueurs_tournoi()
            self.choix_menu_rapport_liste_joueurs()
        elif option == AFFICHER_TOURNOIS:
            self.vue.effacer_ecran()
            self.vue.afficher_tournoi(self.controle.recuperer_tournois_trier_tableau(NOM))
            self.vue.pause_ecran()
        elif option == AFFICHER_TOURS_TOURNOI:
            pass
        elif option == AFFICHER_MATCH_TOURNOI:
            pass
        elif option == RETOUR_MENU_GLOBAL_3:
            self.choix_menu_global()

    def choix_menu_rapport_liste_joueurs(self):
        option = self.vue.entrer_choix_menu()
        if option == AFFICHER_JOUEURS_ALPHA:
            self.vue.effacer_ecran()
            self.vue.afficher_joueurs_trier(self.controle.recuperer_joueurs_trier_tableau(NOM))
            self.vue.pause_ecran()
        elif option == AFFICHER_JOUEURS_CLASSEMENT:
            self.vue.effacer_ecran()
            self.vue.afficher_joueurs_trier(self.controle.recuperer_joueurs_trier_tableau(CLASSEMENT))
            self.vue.pause_ecran()
        elif option == RETOUR_MENU_RAPPORTS_1:
            self.vue.effacer_ecran()
            self.vue.afficher_menu_rapport()
            self.choix_menu_rapport()

    def choix_menu_rapport_liste_joueurs_tournoi(self):
        option = self.vue.entrer_choix_menu()
        if option == AFFICHER_JOUEURS_TOURNOI_ALPHA:
            pass
        elif option == AFFICHER_JOUEURS_TOURNOI_CLASSEMENT:
            pass
        elif option == RETOUR_MENU_RAPPORTS_2:
            self.vue.effacer_ecran()
            self.vue.afficher_menu_rapport()
            self.choix_menu_rapport()
