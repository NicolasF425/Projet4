from views.rounds_view import RoundsView


class TournamentRoundsUpdateController:

    def __init__(self):
        pass

    def print_view(self, tournoi):
        rounds_view = RoundsView()
        liste_infos_rounds = []
        for round in tournoi.rounds:
            infos_round = []
            infos_round = round.to_list()
            liste_infos_rounds.append(infos_round)
        rounds_view.print_rounds_matchs(liste_infos_rounds)
