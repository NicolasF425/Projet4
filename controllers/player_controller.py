from models.player import Player
from views.player_view import PlayerView, AddPlayerView
from utilities import players_manager as pm


class PlayerController:

    ELEMENTS_MENU = ["1/ Créer un nouveau joueur\n", "2/ lister les joueurs\n", "3/ Exporter la liste des joueurs\n",
                     "4/ RETOUR\n"]
    RETOUR = 4

    def __init__(self):
        self.view = PlayerView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = self.view.input_choice()
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
            players = pm.load_players("joueurs.json")
            # on ajoute le nouveau joueur a la liste
            players.append(player)
            # on met a jour le fichier des joueurs
            pm.save_players(players, "joueurs.json")
        except Exception as e:
            print(f"Erreur de sauvegarde : {e}")

    @classmethod
    def list_players(self):
        try:
            players = pm.load_players("joueurs.json")
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
