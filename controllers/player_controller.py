from time import sleep
from os import path
from models.player import Player
from views.player_view import PlayerView, AddPlayerView, ListPlayersView
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
        if choix == 1:
            view = AddPlayerView()
            player_datas = view.add_new_player()
            self.create_player(player_datas[0], player_datas[1], player_datas[2], player_datas[3])
        if choix == 2:
            view = ListPlayersView()
            players = pm.load_players(self.FILENAME)
            view.list_players(players)
            sleep(5)
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
            sleep(3)
        except Exception as e:
            print(f"Erreur de fichier : {e}")

    @classmethod
    def list_players(self):
        try:
            players = pm.load_players(self.FILENAME)
            return players
        except Exception as e:
            print(f"Erreur de recuperation des joueurs : {e}")

    @classmethod
    def check_name(self, name):
        if name == "":
            print("Le nom ne peut etre vide !")
            return None

    @classmethod
    def check_firstname(self, firstname):
        if firstname == "":
            print("le prenom ne peut etre vide !")
            return None

    @classmethod
    def check_birthdate(self, birthdate):
        pass

    @classmethod
    def check_idclub(self, idclub):
        pass

    @classmethod
    def sort_by_name(self, players):
        sorted_players = sorted(players, key=lambda player: player.nom)
        return sorted_players
