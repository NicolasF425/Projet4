from utilities.clear_screen import clear_screen
from views.menu_view import MenuView
from views.list_view import List_view


class TournamentView(MenuView):
    '''Vue du menu de gestion des tournois'''

    TITRE_VUE = "GESTION DES TOURNOIS\n--------------------\n"

    def __init__(self, elements_menu):
        self.titre_vue = self.TITRE_VUE
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)


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


class ListTournamentsView(List_view):

    TITRE_VUE = "LISTE DES TOURNOIS\n------------------\n"
    HEADER = ["Num", "Nom", "Lieu", "Date début", "date fin", "Description"]
    LARGEURS_COLONNES = [4, 20, 20, 10, 10, 80]

    def __init__(self):
        '''retour = 0 si pas sélection affichage simple'''
        '''retour = 1 si sélection dans la liste'''
        clear_screen()
        print(self.TITRE_VUE)

    def list_tournaments(self, listes_tournois, retour=""):
        self.print_line(self.HEADER, self.LARGEURS_COLONNES)
        print("\n")
        for tournoi in listes_tournois:
            self.print_line(tournoi, self.LARGEURS_COLONNES)
        if retour == "":
            input("\nAppuyez sur entrée...")
            return retour
        else:
            retour = input("\nSélectionner le tournoi numéro: ")
            return retour


class PlayerSelectionView(List_view):
    '''Vue pour la selection des joueurs'''

    TITRE_VUE = "SELECTION DES JOUEURS\n---------------------\n"
    HEADER = ["Num", "Nom", "Prenom", "Date naissance", "Club"]
    LARGEURS_COLONNES = [4, 20, 20, 14, 7, 0, 0]
    joueurs = []

    def __init__(self):
        pass

    def print_vue(self, liste_joueurs_fichier, liste_selection_joueurs):
        clear_screen()
        print(self.TITRE_VUE)
        self.print_line(self.HEADER, self.LARGEURS_COLONNES)
        self.print_list(liste_joueurs_fichier, self.LARGEURS_COLONNES)
        self.print_selection_header()
        self.print_list(liste_selection_joueurs, self.LARGEURS_COLONNES)

    def list_players(self, joueurs):
        self.joueurs = joueurs
        for joueur in joueurs:
            elements = joueurs.to_list()
            self.print_line(elements, self.LARGEURS_COLONNES)

    def print_selection_header(self):
        print("\nJOUEURS SELECTIONNES :\n")

    def select_players(self):
        selection = input("\nNuméro d'un joueurs à sélectionner (Entrée pour quitter la sélection) : ")
        return selection
