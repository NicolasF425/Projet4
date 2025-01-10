from time import sleep
from os import path
from utilities import constantes
from views.reports_view import ReportsMenuView, ReportPlayersList, ReportTournamentsList
from views.reports_view import ReportTournamentPlayersView, ReportTournamentRoundsMatchsView
from utilities import players_manager as pm, tournaments_manager as tm


class ReportController:

    FICHIER_JOUEURS = constantes.FICHIER_JOUEURS
    FICHIER_TOURNOIS = constantes.FICHIER_TOURNOIS
    ELEMENTS_MENU = ["1/ lister les joueurs\n", "2/ Lister les tournois\n", "3/ Retour\n"]
    RETOUR = len(ELEMENTS_MENU)

    def __init__(self):
        self.view = ReportsMenuView(self.ELEMENTS_MENU)
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
                    for joueur in joueurs:
                        infos_joueur = joueur.to_list()
                        listes_infos_joueurs.append(infos_joueur)
                    view.list_players(listes_infos_joueurs)
            else:
                print("Fichier des joueurs non trouvé")
                sleep(2)

        # liste des tournois
        if choix == 2:
            numero_tournoi = 0
            view = ReportTournamentsList()
            if path.exists(self.FICHIER_TOURNOIS) is True:
                tournois = tm.load_tournaments(self.FICHIER_TOURNOIS)
                # s'il y a un ou des tournois
                if tournois is not None:
                    listes_infos_tournois = []
                    for tournoi in tournois:
                        infos_tournoi = tournoi.to_list()
                        listes_infos_tournois.append(infos_tournoi)
                    retour = view.list_tournaments(listes_infos_tournois)
                    # si on a choisi un tournoi
                    if retour != "" and retour != constantes.ESCAPE:
                        try:
                            numero_tournoi = int(retour)
                            # on enleve 1 car l'indice commence a 0 et les tournois a 1
                            indice_tournoi = numero_tournoi-1
                            # affichage des joueurs
                            joueurs_tournoi = self.sort_by_name(tournois[indice_tournoi].joueurs)
                            listes_infos_joueurs = []
                            for joueur in joueurs_tournoi:
                                infos_joueur = joueur.to_list()
                                listes_infos_joueurs.append(infos_joueur)
                            players_view = ReportTournamentPlayersView()
                            players_view.print_player_list(listes_infos_joueurs)

                            # affichage des rounds et des matchs
                            rounds_view = ReportTournamentRoundsMatchsView()
                            liste_infos_rounds = []
                            for round in tournois[indice_tournoi].rounds:
                                infos_round = round.to_list()
                                liste_infos_rounds.append(infos_round)
                            rounds_view.print_rounds_matchs(liste_infos_rounds)

                        except ValueError:
                            print("Vous devez entrer un nombre !")
                            sleep(2)
                        except Exception as err:
                            print(f"Erreur {err} !")
                            sleep(5)
            else:
                print("Fichier des tournois non trouvé")
                sleep(2)

        # Retour
        if choix == self.RETOUR:
            return choix

    def sort_by_name(self, joueurs):
        '''Trie les joueurs par nom et par ordre alphabétique'''
        sorted_players = sorted(joueurs, key=lambda player: player.nom)
        return sorted_players
