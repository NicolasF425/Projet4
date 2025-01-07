import sys
from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.reports_controller import ReportController


class MainController:
    '''Classe pour la gestion du menu principal'''

    ELEMENTS_MENU = ["1/ Gestion des joueurs\n", "2/ Gestion des tournois\n", "3/ Rapports\n", "4/ Quitter\n"]
    QUITTER = 4

    def __init__(self):
        self.view = MainView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = 0
        while choix is not self.QUITTER:
            choix = self.view.input_choice()
            # gestion des joueurs
            if choix == 1:
                retour = 0
                player_controller = PlayerController()
                while retour is not player_controller.RETOUR:
                    retour = player_controller.manage_input()
            # gestion des tournois
            if choix == 2:
                retour = 0
                tournament_controller = TournamentController()
                while retour is not tournament_controller.RETOUR:
                    retour = tournament_controller.manage_input()
            # gestion des rapports
            if choix == 3:
                retour = 0
                report_controller = ReportController()
                while retour is not report_controller.RETOUR:
                    retour = report_controller.manage_input()
        sys.exit(1)
