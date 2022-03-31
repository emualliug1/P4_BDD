# -*- coding:Utf8 -*-
#############################################
# Programme Python type
# Auteur: G.T,Nt,2022
#############################################
# Importation de fonction externe :
from tinydb import TinyDB
from tinydb import table
from tinydb import Query
#############################################
# Définition des constantes
NOM = 'Nom'
LIEU = 'Lieu'
DATE_TOURNOI = 'Date du tournoi'
CONTROLE_TEMPS = 'Controle du temps'
DESCRIPTION = 'Description'
JOUEURS_TOURNOI = 'Joueurs du tournoi'
PRENOM = 'Prenom'
DATE_NAISSANCE = 'Date de naissance'
SEXE = 'Sexe'
CLASSEMENT = 'Classement'
JOUEURS = 'Joueurs'
TOURNOI = 'Tournoi'
NOM_BDD = 'bdd_tournoi.json'
# Définition de la classe


class Modele:

    def __init__(self, tournoi, joueur, ronde, match):
        self.tournoi = tournoi
        self.joueur = joueur
        self.ronde = ronde
        self.match = match
        self.db_maitre = TinyDB(NOM_BDD)
        self.db_tournoi_table = self.db_maitre.table(TOURNOI)
        self.db_joueur_table = self.db_maitre.table(JOUEURS)
        self.query = Query()

    def sauvegarder_db_tournoi(self) -> [TinyDB.table]:
        """Sauvegarde les informations des tournois dans une table d'une BDD"""
        self.db_tournoi_table.insert_multiple([self.tournoi.dictionnaire_tournoi()])
        return self.db_tournoi_table

    def sauvegarder_db_joueurs(self) -> [TinyDB.table]:
        """Sauvegarde les informations des joueurs dans une table d'une BDD"""
        self.db_joueur_table.insert_multiple([self.joueur.dictionnaire_joueur()])
        return self.db_joueur_table

    def enregistrer_db_tournoi_ronde(self, id_tournoi):
        """Enregistre une ronde d'un tournoi dans la BDD"""
        self.db_tournoi_table.upsert(table.Document({self.ronde.id_ronde: self.ronde.ronde_liste}, doc_id=id_tournoi))

    def enregistrer_db_tournoi_joueurs(self, id_tournoi):
        """Enregistre la liste des joueurs du tournoi dans la BDD"""
        self.db_tournoi_table.upsert(table.Document({JOUEURS_TOURNOI: self.tournoi.joueurs_tournoi}, doc_id=id_tournoi))

    def enregistrer_db_tournoi_modifier(self, id_tournoi):
        """Enregistre la modification d'un tournoi dans la BDD"""
        self.db_tournoi_table.update(self.tournoi.dictionnaire_tournoi(), doc_ids=[id_tournoi])

    def enregistrer_db_joueur_modifier(self, id_joueur):
        """Enregistre la modification d'un joueur dans la BDD"""
        self.db_joueur_table.update(self.joueur.dictionnaire_joueur(), doc_ids=[id_joueur])
