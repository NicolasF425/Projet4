import sys
from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


class MainController:

    ELEMENTS_MENU = ["1/ Gestion des joueurs\n", "2/ Gestion des tournois\n", "3/ Quitter\n"]
    QUITTER = 3

    def __init__(self):
        self.view = MainView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = 0
        while choix is not self.QUITTER:
            choix = self.view.input_choice()
            if choix == 1:
                retour = 0
                player_controller = PlayerController()
                while retour is not player_controller.RETOUR:
                    retour = player_controller.manage_input()
            if choix == 2:
                retour = 0
                tournament_controller = TournamentController()
                while retour is not tournament_controller.RETOUR:
                    retour = tournament_controller.manage_input()
        sys.exit(1)
