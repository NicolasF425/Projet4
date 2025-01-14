from views.rounds_view import RoundsView
from models.match import Match
from utilities import tournaments_manager as tm
from utilities import constantes
from datetime import datetime
from time import sleep


class TournamentRoundsUpdateController:
    '''Classe pour gérer l'état des scores et des rounds'''

    def __init__(self):
        pass

    def manage_rounds(self, tournoi):

        rounds_view = RoundsView()
        liste_infos_rounds = []

        for round in tournoi.rounds:
            infos_round = []
            infos_round = round.to_list()
            liste_infos_rounds.append(infos_round)
        rounds_view.print_rounds_matchs(liste_infos_rounds)
        round_actuel = tournoi.round_actuel-1

        # si le rounds actuel n'est pas fini
        # on propose l'affectation des scores
        if tournoi.rounds[round_actuel].est_fini == "Non":
            retour = rounds_view.update_score()
            if retour != constantes.ESCAPE:
                indice_match = int(retour[0])-1
                match = Match()
                if tournoi.rounds[round_actuel].matchs[indice_match] != "Non":
                    numero_premier_joueur = tournoi.rounds[round_actuel].matchs[indice_match].scores_joueurs[0][0]
                    numero_second_joueur = tournoi.rounds[round_actuel].matchs[indice_match].scores_joueurs[1][0]
                    # onm met a jour les scores du match
                    scores_joueurs = ([numero_premier_joueur, retour[1]], [numero_second_joueur, retour[2]])
                    # on met a jour le nombrs de points des joueurs
                    tournoi.rounds[round_actuel].joueurs[numero_premier_joueur-1].score += float(retour[1])
                    tournoi.rounds[round_actuel].joueurs[numero_second_joueur-1].score += float(retour[2])
                    tournoi.joueurs[numero_premier_joueur-1].score += float(retour[1])
                    tournoi.joueurs[numero_second_joueur-1].score += float(retour[2])
                    match.scores_joueurs = scores_joueurs
                    match.est_fini = "Oui"
                    tournoi.rounds[round_actuel].matchs[indice_match] = match

                # on verifie si tous les matchs sont finis
                # on met a jour le round si c'est le cas
                if self.check_all_matchs_finished(tournoi.rounds[round_actuel]) == "Oui":
                    tournoi.rounds[round_actuel].est_fini = "Oui"
                    maintenant = datetime.now()
                    date_heure = maintenant.strftime("%d/%m/%Y, %H:%M")
                    tournoi.rounds[round_actuel].set_date_heure_fin(date_heure)
                    if self.check_all_rounds_finished(tournoi):
                        tournoi.en_cours = "Non"

                # sauvegarde du tournoi créé
                tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
                tournois[tournoi.numero_tournoi-1] = tournoi
                tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)
        # si le round actuel est fini
        else:
            print("Pas de round actif !")
            sleep(2)

    def check_all_matchs_finished(self, round):
        '''Vérfie si tous les matchs du round en paramètre sont finis'''
        matchs_finis = "Oui"
        for match in round.matchs:
            if match.est_fini == "Non":
                matchs_finis = "Non"
                break
        return matchs_finis

    def check_all_rounds_finished(self, tournoi):
        '''Vérifie si tous les rounds du tournoi en paramètre sont finis'''
        tous_rounds_finis = True
        for round in tournoi.rounds:
            if round.est_fini == "Non":
                tous_rounds_finis = False
                return tous_rounds_finis
        return tous_rounds_finis
