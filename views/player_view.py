from utilities.clear_screen import clear_screen
from utilities import constantes
from views.menu_view import MenuView
from views.list_view import ListView


class PlayerMenuView(MenuView):
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
        while self.check_nom(self.nom) is not True and self.nom != constantes.ESCAPE:
            self.nom = input("Nom : ")
            if self.nom == constantes.ESCAPE:
                return constantes.ESCAPE

        self.prenom = input("Prenom : ")
        while self.check_nom(self.prenom) is not True and self.prenom != constantes.ESCAPE:
            self.prenom = input("Prenom : ")
            if self.prenom == constantes.ESCAPE:
                return constantes.ESCAPE

        self.date_de_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
        while self.check_date_de_naissance(self.date_de_naissance) is not True and \
                self.date_de_naissance != constantes.ESCAPE:
            self.date_de_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
            if self.date_de_naissance == constantes.ESCAPE:
                return constantes.ESCAPE

        self.identifiant_club = input("identifiant du club :")
        while self.check_identifiant_club(self.identifiant_club) is not True and \
                self.identifiant_club != constantes.ESCAPE:
            self.identifiant_club = input("identifiant du club :")
            if self.identifiant_club == constantes.ESCAPE:
                return constantes.ESCAPE

        self.datas_player = [self.nom, self.prenom, self.date_de_naissance, self.identifiant_club]
        return self.datas_player

    def check_nom(self, nom):
        if nom == "":
            print("Le nom ne peut etre vide !")
            return False
        return True

    def check_prenom(self, prenom):
        if prenom == "":
            print("le prenom ne peut etre vide !")
            return False
        return True

    def check_date_de_naissance(self, date_de_naissance):
        longueur = len(date_de_naissance)
        if longueur < 10 or longueur > 10:
            print("date de naissance mal formatée !")
            return False
        return True

    def check_identifiant_club(self, identifiant_club):
        longueur = len(identifiant_club)
        if longueur < 7 or longueur > 7:
            print("Identifiant du club mal formaté !")
            return False
        return True


class ListPlayersView(ListView):
    '''Vue pour la liste des joueurs'''

    TITRE_VUE = "LISTE DES JOUEURS PAR ORDRE ALPHABETIQUE\n----------------------------------------\n"
    HEADER = ["Num", "Nom", "Prenom", "Date naissance", "Club"]
    LARGEURS_COLONNES = [4, 20, 20, 14, 7, 0, 0]

    def __init__(self):
        clear_screen()
        print(self.TITRE_VUE)

    def list_players(self, listes_infos_joueurs):
        self.print_line(self.HEADER, self.LARGEURS_COLONNES)
        print("\n")
        for infos_joueurs in listes_infos_joueurs:
            self.print_line(infos_joueurs, self.LARGEURS_COLONNES)
        input("\nAppuyez sur entrée...")
