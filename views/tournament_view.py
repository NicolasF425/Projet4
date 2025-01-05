from utilities.clear_screen import clear_screen
from views.menu_view import MenuView


class Commons:
    '''Classe pour fonctions communes'''

    # ecrit une ligne formatee pour un joueur
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


class TournamentView(Commons, MenuView):
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

    def select_players(self):
        selection = input("\nNuméro d'un joueurs à sélectionner (Entrée pour quitter la sélection) : ")
        return selection


class TournamentSummaryView(Commons):
    '''Résume les paramètres entrés pour le tournoi'''

    def __init__(self):
        pass

    def print_summary(self, tournament):
        clear_screen()
        for joueur in tournament.players:
            self.print_player(joueur)
