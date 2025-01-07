from time import sleep
from os import path
from utilities import constantes
from views.reports_view import ReportsView, ReportPlayersList, ReportTournamentsList
from utilities import players_manager as pm, tournaments_manager as tm


class ReportController:

    FICHIER_JOUEURS = constantes.FICHIER_JOUEURS
    FICHIER_TOURNOIS = constantes.FICHIER_TOURNOIS
    ELEMENTS_MENU = ["1/ lister les joueurs\n", "2/ Lister les tournois\n", "3/ Retour\n"]
    RETOUR = len(ELEMENTS_MENU)

    def __init__(self):
        self.view = ReportsView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = self.view.input_choice()

        # Liste des joueurs par ordre alphabetique
        if choix == 1:
            view = ReportPlayersList()
            if path.exists(self.FICHIER_JOUEURS) is True:
                joueurs = pm.load_players(self.FICHIER_JOUEURS)
                if joueurs is not None:
                    joueurs = self.sort_by_name(joueurs)
                    listes_infos_joueurs = []
                    for infos_joueur in joueurs:
                        listes_infos_joueurs.append(infos_joueur.to_list())
                    view.list_players(listes_infos_joueurs)
            else:
                print("Fichier des joueurs non trouvé")
                sleep(2)

        # liste des tournois
        if choix == 2:
            view = ReportTournamentsList()
            if path.exists(self.FICHIER_TOURNOIS) is True:
                tournois = tm.load_tournaments(self.FICHIER_TOURNOIS)
                if tournois is not None:
                    listes_infos_tournois = []
                    for infos_tournoi in tournois:
                        listes_infos_tournois.append(infos_tournoi.to_list())
                    view.list_tournaments(listes_infos_tournois)
            else:
                print("Fichier des tournois non trouvé")
                sleep(2)

        # Retour
        if choix == self.RETOUR:
            return choix

    def sort_by_name(self, players):
        '''Trie les joueurs par nom et par ordre alphabétique'''
        sorted_players = sorted(players, key=lambda player: player.nom)
        return sorted_players
