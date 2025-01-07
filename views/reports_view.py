from views.menu_view import MenuView
from views.player_view import ListPlayersView
from views.tournament_view import ListTournamentsView


class ReportsMenuView(MenuView):
    '''Vue du menu de gestion des rapports'''

    TITRE_VUE = "RAPPORTS\n-------------------\n"

    def __init__(self, elements_menu):
        self.titre_vue = self.TITRE_VUE
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)


class ReportPlayersList(ListPlayersView):

    def __init__(self):
        super().__init__()


class ReportTournamentsList(ListTournamentsView):

    def __init__(self):
        super().__init__()
