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
            if retour == constantes.ESCAPE:
                return constantes.ESCAPE
            # controle des entrees
            if self.check_scores(retour, tournoi) == "Non":
                return "Non"
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
                    tous_matchs_finis = self.check_all_matchs_finished(tournoi.rounds[round_actuel])
                    if tous_matchs_finis == "Oui":
                        tournoi.rounds[round_actuel].est_fini = "Oui"
                        maintenant = datetime.now()
                        date_heure = maintenant.strftime("%d/%m/%Y, %H:%M")
                        tournoi.rounds[round_actuel].set_date_heure_fin(date_heure)

                        # on vérifie si tous les rounds sont finis
                        if (round_actuel+1) == tournoi.nombre_de_rounds:
                            if tournoi.rounds[round_actuel].est_fini:
                                tournoi.en_cours = "Non"
                                print("\nFIN DU MATCH !!!\nMerci de consulter le rapport de ce match !")
                                sleep(3)

                    # sauvegarde du tournoi
                    tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
                    tournois[tournoi.numero_tournoi-1] = tournoi
                    tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)

                    return tous_matchs_finis
                else:
                    print("Ce match est fini !")
                    sleep(2)
                    return ("Non")
        # si le round actuel est fini
        else:
            print("Pas de round actif !")
            sleep(2)

    def check_scores(self, retour, tournoi):
        try:
            # test si on a bien entré un nombre
            int(retour[0])
        except ValueError:
            print("Vous devez entrer un numéro de match :")
            sleep(2)
            return "Non"
        if int(retour[0]) > len(tournoi.rounds[tournoi.round_actuel-1].matchs):
            print("Numéro de match incorrect !")
            sleep(2)
            return "Non"
        if (retour[1] != "1" and retour[1] != "0.5" and retour[1] != "0" and retour[2] != "1" and retour[2] != "0.5"
                and retour[2] != "0"):
            print("Valeurs de scores incorrectes")
            sleep(2)
            return "Non"
        total_scores = float(retour[1]) + float(retour[2])
        if total_scores < 1 or total_scores > 1:
            print("Valeurs de scores incorrectes")
            sleep(2)
            return "Non"

    def check_all_matchs_finished(self, round):
        '''Vérfie si tous les matchs du round en paramètre sont finis'''
        matchs_finis = "Oui"
        for match in round.matchs:
            if match.est_fini == "Non":
                matchs_finis = "Non"
                break
        return matchs_finis
