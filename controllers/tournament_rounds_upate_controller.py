from views.rounds_view import RoundsView
from models.match import Match
from utilities import tournaments_manager as tm
from utilities import constantes


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
        round_actuel = tournoi.round_actuel-1
        if tournoi.rounds[round_actuel].est_fini == "Non":
            retour = rounds_view.update_score()
            indice_match = int(retour[0])-1
            match = Match()
            if tournoi.rounds[round_actuel].matchs[indice_match] != "Non":
                numero_premier_joueur = tournoi.rounds[round_actuel].matchs[indice_match].scores_joueurs[0][0]
                numero_second_joueur = tournoi.rounds[round_actuel].matchs[indice_match].scores_joueurs[1][0]
                scores_joueurs = ([numero_premier_joueur, retour[1]], [numero_second_joueur, retour[2]])
                match.scores_joueurs = scores_joueurs
                match.est_fini = "Oui"

                tournoi.rounds[round_actuel].matchs[indice_match] = match

            # sauvegarde du tournoi créé
            tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
            tournois[tournoi.numero_tournoi-1] = tournoi
            tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)
