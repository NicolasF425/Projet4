from utilities.clear_screen import clear_screen
from views.menu_view import MenuView
from views.list_view import ListView
from utilities import constantes


class TournamentMenuView(MenuView):
    '''Vue du menu de gestion des tournois'''

    TITRE_VUE = "GESTION DES TOURNOIS\n--------------------\n"

    def __init__(self, elements_menu):
        self.titre_vue = self.TITRE_VUE
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)


class TournamentDisplayView(ListView, MenuView):

    TITRE_VUE = "MODIFIER LE TOURNOI\n-------------------\n"

    def __init__(self, elements_menu):
        self.titre_vue = self.TITRE_VUE
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)

    def print_tournament(self, tournament_infos, players_infos):
        clear_screen()
        print(self.TITRE_VUE)
        self.print_tournament_infos(tournament_infos)
        print("\n")
        self.print_tournament_players_infos(players_infos)
        print("\n")

    def print_tournament_infos(self, tournament_infos):
        if type(tournament_infos) is list:
            if len(tournament_infos) == 9:
                print("Numéro : ",  tournament_infos[0])
                print("Nom : ", tournament_infos[1])
                print("Lieu : ", tournament_infos[2])
                print("Date de début : ", tournament_infos[3])
                print("Date de fin : ", tournament_infos[4])
                print("Nombre de rounds : ", tournament_infos[5])
                print("Round en cours : ", tournament_infos[6])
                print("En cours : ", tournament_infos[7])
                print("Description : ", tournament_infos[8])
        else:
            print("Données tournoi insuffisantes")

    def print_tournament_players_infos(self, players_infos):
        HEADER = ["Num", "Nom", "Prenom", "Date naissance", "Club"]
        LARGEURS_COLONNES = [4, 20, 20, 14, 7, 0, 0]
        self.print_line(HEADER, LARGEURS_COLONNES)
        self.print_list(players_infos, LARGEURS_COLONNES)


class NewTournamentView:

    def __init__(self):
        clear_screen()

    def param_tournament(self):
        print("CREATION D'UN NOUVEAU TOURNOI\n-----------------------------\n")
        nom = input("Nom :")
        if nom == constantes.ESCAPE:
            return constantes.ESCAPE
        lieu = input("Lieu :")
        if lieu == constantes.ESCAPE:
            return constantes.ESCAPE
        date_debut = input("Date de début :")
        if date_debut == constantes.ESCAPE:
            return constantes.ESCAPE
        date_fin = input("Date de fin :")
        if date_fin == constantes.ESCAPE:
            return constantes.ESCAPE
        nombre_de_rounds = input("Nombre de rounds :")
        if nombre_de_rounds == constantes.ESCAPE:
            return constantes.ESCAPE
        description = input("Description :")
        if description == constantes.ESCAPE:
            return constantes.ESCAPE
        datas_tournament = [nom, lieu, date_debut, date_fin, nombre_de_rounds, description]
        return datas_tournament


class ListTournamentsView(ListView):

    TITRE_VUE = "LISTE DES TOURNOIS\n------------------\n"
    HEADER = ["Num", "Nom", "Lieu", "Début", "Fin", "Rounds", "Actuel", "En cours", "Description"]
    LARGEURS_COLONNES = [4, 20, 20, 10, 10, 6, 6, 8, 60]

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


class PlayerSelectionView(ListView):
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
        self.print_selection_header(len(liste_selection_joueurs))
        self.print_list(liste_selection_joueurs, self.LARGEURS_COLONNES)

    def list_players(self, joueurs):
        self.joueurs = joueurs
        for joueur in joueurs:
            elements = joueurs.to_list()
            self.print_line(elements, self.LARGEURS_COLONNES)

    def print_selection_header(self, nombre=0):
        if nombre > 0:
            n = str(nombre)
        else:
            n = ""
        print("\nJOUEURS SELECTIONNES : "+n+"\n")

    def select_players(self):
        selection = input("\nNuméro d'un joueurs à sélectionner (Entrée pour quitter la sélection) : ")
        return selection
