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

    SPACES = "                              "
    LARGEUR_COLONNE = 15

    def __init__(self):
        clear_screen()

    def list_players(self):
        players = PC.list_players()
        for player in players:
            player.print_player()

    @classmethod
    def print_player_header(self):
        print("Nom" + self.SPACES[0:self.LARGEUR_COLONNE-3] + "|"
              + "Prenom" + self.SPACES[0:self.LARGEUR_COLONNE-6] + "|"
              + "Date de naissance|"
              + "Club"+"\n")

    def print_player(self, player):
        temp_nom = player.nom
        temp_prenom = player.prenom
        delta_nom = len(temp_nom)-self.LARGEUR_COLONNE
        delta_prenom = len(temp_prenom)-self.LARGEUR_COLONNE
        if delta_nom < 0:   # nom plus court que largeur colonne
            temp_nom = temp_nom + self.SPACES[0:-delta_nom]
        else:
            temp_nom = temp_nom[0:self.LARGEUR_COLONNE]

        if delta_prenom < 0:
            temp_prenom = temp_prenom + self.SPACES[0:-delta_prenom]
        else:
            temp_prenom = temp_prenom[0:self.LARGEUR_COLONNE]

        print(temp_nom + "|" +
              temp_prenom + "|" +
              player.date_de_naissance + "       |" +
              player.identifiant_club)

    def list_players_by_name(self):
        players = PC.list_players()
        sorted_players = PC.sort_by_name(players)
        self.print_player_header()
        for player in sorted_players:
            self.print_player(player)
