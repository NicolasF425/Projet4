from time import sleep
from utilities.clear_screen import clear_screen


class PlayerView:

    TITRE_VUE = "GESTION DES JOUEURS\n"

    def __init__(self, elements_menu):
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)

    def print_view(self):
        clear_screen()
        print(self.TITRE_VUE)
        for item in self.elements_menu:
            print(item)

    def input_choice(self):
        choix_ok = False
        while choix_ok is False:
            self.print_view()
            choix = input("\nSélectioner : ")
            choix_ok = self.check_choix(choix)
        return int(choix)

    def check_choix(self, choix):
        try:
            choix = int(choix)
        except ValueError:
            print("Veuillez Entrer un nombre !")
            sleep(2)
            return False
        if choix > 0 and choix <= self.nb_elements:
            return True
        else:
            print("Vous devez choisir une option de 1 à "+str(self.nb_elements))
            sleep(2)
            return False


class AddPlayerView:

    TITRE_VUE = "AJOUTER UN JOUEUR\n"

    nom = ""
    prenom = ""
    date_de_naissance = ""
    identifiant_club = ""

    def __init__(self):
        clear_screen()
        print(self.TITRE_VUE)

    def add_new_player(self):
        print("Creation du nouveau joueur")
        self.nom = input("Nom : ")
        self.prenom = input("Prenom : ")
        self.date_de_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
        self.identifiant_club = input("identifiant du club :")
        self.datas_player = [self.nom, self.prenom, self.date_de_naissance, self.identifiant_club]
        return self.datas_player


class ListPlayersView:

    SPACES = "                              "
    LARGEUR_COLONNE = 15

    def __init__(self):
        clear_screen()

    def list_players(self, players):
        for player in players:
            self.print_player(player)

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
