from time import sleep
from utilities.clear_screen import clear_screen


class TournamentView:
    '''Vue du menu de gestion des tournois'''

    TITRE_VUE = "GESTION DES TOURNOIS\n--------------------\n"

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


class NewTournamentView:

    def __init__(self):
        clear_screen()

    def param_tournament(self):
        print("CREATION D'UN NOUVEAU TOURNOI\n-----------------------------\n")
        nom = input("Nom :")
        lieu = input("Lieu :")
        date_debut = input("Date de début :")
        date_fin = input("Date de fin :")
        nombre_de_rounds = input("Nombre de rounds :")
        description = input("Description :")
        datas_tournament = [nom, lieu, date_debut, date_fin, nombre_de_rounds, description]
        return datas_tournament


class PlayerSelectionView:
    '''Vue pour la selection des joueurs'''

    TITRE_VUE = "SELECTION DES JOUEURS\n---------------------\n"
    SPACES = "                              "
    LARGEUR_COLONNE = 15

    players = []

    def __init__(self):
        pass

    def print_vue(self, joueurs_fichier, selection_joueurs):
        clear_screen()
        print(self.TITRE_VUE)
        self.print_player_header()
        self.list_players(joueurs_fichier)
        self.print_selection_header()
        self.list_players(selection_joueurs)

    def list_players(self, joueurs):
        self.players = joueurs
        for player in joueurs:
            self.print_player(player)

    def print_player_header(self):
        print("    |" + "Nom" + self.SPACES[0:self.LARGEUR_COLONNE-3] + "|"
              + "Prenom" + self.SPACES[0:self.LARGEUR_COLONNE-6] + "|"
              + "Date de naissance|"
              + "Club"+"\n")

    def print_selection_header(self):
        print("\nJOUEURS SELECTIONNES :\n")

    def print_player(self, joueur):
        temp_nom = joueur.nom
        temp_prenom = joueur.prenom
        numero = joueur.numero_joueur
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

        print(str(numero)+self.SPACES[0:4-len(str(numero))] + "|" + temp_nom + "|"
              + temp_prenom + "|" +
              joueur.date_de_naissance + "       |" +
              joueur.identifiant_club)

    def select_players(self):
        selection = input("\nNuméro d'un joueurs à sélectionner (Entrée pour quitter la sélection) : ")
        return selection
