from controllers.player_controller import PlayerController as PC
from utilities.clear_screen import clear_screen


class AddPlayerView:

    nom = ""
    prenom = ""
    date_de_naissance = ""
    identifiant_club = ""

    def __init__(self):
        clear_screen()

    def add_new_player(self):
        print("Creation du nouveau joueur")
        self.nom = input("Nom : ")
        self.prenom = input("Prenom : ")
        self.date_de_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
        self.identifiant_club = input("identifiant du club :")
        PC.create_player(self.nom, self.prenom,
                         self.date_de_naissance, self.identifiant_club)


class ListPlayersView:

    def __init__(self):
        clear_screen()

    def list_players(self):
        players = PC.list_players()
        for player in players:
            player.print_player()

    def list_players_by_name(self):
        players = PC.list_players()
        sorted_players = PC.sort_by_name(players)
        for player in sorted_players:
            player.print_player()
