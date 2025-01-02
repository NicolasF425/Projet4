from views.tournament_view import TournamentView, NewTournamentView, PlayerSelectionView
from models.tournament import Tournament
from utilities import players_manager as pm
from time import sleep


class TournamentController:

    FILENAME = "joueurs.json"
    ELEMENTS_MENU = ["1/ Créer un nouveau tournoi\n", "2/ Mettre à jour un tournoi\n", "3/ Lister les tournois\n",
                     "4/ RETOUR\n"]
    RETOUR = 4

    def __init__(self):
        self.view = TournamentView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = self.view.input_choice()

        # Nouveau tournoi
        if choix == 1:
            tournoi = Tournament()
            # Entree des infos nom, lieu, date debut et date fin
            next = False
            while next is False:
                view = NewTournamentView()
                datas = view.param_tournament()
                next = self.check_tournament_datas(datas)
            tournoi.nom = datas[0]
            tournoi.lieu = datas[1]
            tournoi.date_debut = datas[2]
            tournoi.date_fin = datas[3]
            tournoi.nombre_de_rounds = datas[4]
            tournoi.description = datas[5]
            # si ok on passe a la selection des joueurs
            view = PlayerSelectionView()
            view.print_player_header()
            players = pm.load_players(self.FILENAME)
            view.list_players(players)
            while view.select_players() != "":
                pass

        # Modification de tournoi existant
        if choix == 2:
            pass

        # Liste des tournois
        if choix == 3:
            pass

        # Retour
        if choix == self.RETOUR:
            return choix

    def check_nom(self, nom):
        if nom == "":
            print("Le nom ne peut etre vide !")
            return False
        return True

    def check_lieu(self, lieu):
        if lieu == "":
            print("Le lieu ne peut etre vide !")
            return False
        return True

    def check_date(self, date):
        longueur = len(date)
        if longueur < 10 or longueur > 10:
            print("Date  mal formatée !")
            return False
        return True

    def check_tournament_datas(self, tournament_datas):
        nom = tournament_datas[0]
        lieu = tournament_datas[1]
        date_debut = tournament_datas[2]
        date_fin = tournament_datas[3]
        print("")
        nom_ok = self.check_nom(nom)
        lieu_ok = self.check_lieu(lieu)
        date_debut_ok = self.check_date(date_debut)
        date_fin_ok = self.check_date(date_fin)
        if (nom_ok and lieu_ok and date_debut_ok and date_fin_ok):
            return True
        sleep(2)
        return False
