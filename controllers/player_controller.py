from time import sleep
from datetime import date
from os import path
from models.player import Player
from views.player_view import PlayerView, AddPlayerView, ListPlayersView, ExportPlayersView
from utilities import players_manager as pm


class PlayerController:

    FILENAME = "joueurs.json"
    ELEMENTS_MENU = ["1/ Créer un nouveau joueur\n", "2/ lister les joueurs\n", "3/ Exporter la liste des joueurs\n",
                     "4/ RETOUR\n"]
    RETOUR = 4

    def __init__(self):
        self.view = PlayerView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = self.view.input_choice()

        # Nouveau joueur
        if choix == 1:
            ok = False
            while ok is False:
                view = AddPlayerView()
                player_datas = view.add_new_player()
                ok = self.check_player_datas(player_datas)
            self.create_player(player_datas[0], player_datas[1], player_datas[2], player_datas[3])

        # Liste des joueurs par ordre alphabetique
        if choix == 2:
            view = ListPlayersView()
            joueurs = pm.load_players(self.FILENAME)
            joueurs = self.sort_by_name(joueurs)
            view.list_players(joueurs)
            input("\nAppuyez sur entrée...")

        # Export dans un fichier txt des joueurs par ordre alphabetique
        if choix == 3:
            joueurs = pm.load_players(self.FILENAME)
            joueurs = self.sort_by_name(joueurs)
            fichier_export = "Joueurs_au_"+date.today().strftime("%d%m%Y")+".txt"
            view = ExportPlayersView()
            ok = pm.export_players(fichier_export, joueurs)
            if ok is True:
                view.print_export(len(joueurs))

        # Retour
        if choix == self.RETOUR:
            return choix

    @classmethod
    def create_player(self, Name, FirstName, BirthDate, ClubId):
        '''Sauve la liste des joueurs dans le fichier json'''
        try:
            player = Player(nom=Name, prenom=FirstName,
                            date_de_naissance=BirthDate,
                            identifiant_club=ClubId)
            # on recupere la liste des joueurs du fichier
            players = []
            if path.exists(self.FILENAME) is True:
                players = pm.load_players(self.FILENAME)
            # on ajoute le nouveau joueur a la liste
            players.append(player)
            # on met a jour le fichier des joueurs
            pm.save_players(players, self.FILENAME)
            sleep(2)
        except Exception as e:
            print(f"Erreur de fichier : {e}")

    def list_players(self):
        try:
            players = pm.load_players(self.FILENAME)
            return players
        except Exception as e:
            print(f"Erreur de recuperation des joueurs : {e}")

    def check_nom(self, nom):
        if nom == "":
            print("Le nom ne peut etre vide !")
            return False
        return True

    def check_prenom(self, prenom):
        if prenom == "":
            print("le prenom ne peut etre vide !")
            return False
        return True

    def check_date_de_naissance(self, date_de_naissance):
        longueur = len(date_de_naissance)
        if longueur < 10 or longueur > 10:
            print("date de naissance mal formatée !")
            return False
        return True

    def check_identifiant_club(self, identifiant_club):
        longueur = len(identifiant_club)
        if longueur == 0 or longueur > 7:
            print("Identifiant du club mal formaté !")
            return False
        return True

    def check_player_datas(self, player_datas):
        nom = player_datas[0]
        prenom = player_datas[1]
        date_de_naissance = player_datas[2]
        identifiant_club = player_datas[3]
        print("")
        nom_ok = self.check_nom(nom)
        prenom_ok = self.check_prenom(prenom)
        date_de_naissance_ok = self.check_date_de_naissance(date_de_naissance)
        identifiant_club_ok = self.check_identifiant_club(identifiant_club)
        if (nom_ok and prenom_ok and date_de_naissance_ok and identifiant_club_ok):
            return True
        sleep(2)
        return False

    def sort_by_name(self, players):
        sorted_players = sorted(players, key=lambda player: player.nom)
        return sorted_players
