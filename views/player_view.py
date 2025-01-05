from utilities.clear_screen import clear_screen
from views.menu_view import MenuView


class PlayerView(MenuView):
    '''Vue du menu de gestion des joueurs'''

    TITRE_VUE = "GESTION DES JOUEURS\n-------------------\n"

    def __init__(self, elements_menu):
        self.titre_vue = self.TITRE_VUE
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)


class AddPlayerView:
    '''Vue pour la creation d'un nouveau joueur'''

    TITRE_VUE = "AJOUTER UN JOUEUR\n-----------------\n"

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
    '''Vue pour la liste des joueurs'''

    TITRE_VUE = "LISTE DES JOUEURS\n-----------------\n"
    SPACES = "                              "
    LARGEUR_COLONNE = 15

    def __init__(self):
        clear_screen()
        print(self.TITRE_VUE)

    def list_players(self, players):
        self.print_player_header()
        for player in players:
            self.print_player(player)

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


class ExportPlayersView:
    '''Vue de l'export des joueurs vers un fichier txt'''

    def __init__(self):
        clear_screen()
        print("Export en cours...")

    def print_export(self, nombre_joueurs):
        print(str(nombre_joueurs) + "joueur(s) exporté(s)\n")
        input("\nAppuyez sur entrée...")
