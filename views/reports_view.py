from views.menu_view import MenuView
from views.player_view import ListPlayersView
from views.list_view import ListView
from utilities.clear_screen import clear_screen


class ReportsMenuView(MenuView):
    '''Vue du menu de gestion des rapports'''

    TITRE_VUE = "RAPPORTS\n-------------------\n"

    def __init__(self, elements_menu):
        self.titre_vue = self.TITRE_VUE
        self.elements_menu = elements_menu
        self.nb_elements = len(elements_menu)


class ReportPlayersList(ListPlayersView):
    '''Vue pour la liste des joueurs'''

    def __init__(self):
        super().__init__()


class ReportTournamentsList(ListView):
    '''vus pour la liste des tournois'''

    TITRE_VUE = "LISTE DES TOURNOIS\n------------------\n"
    HEADER = ["Num", "Nom", "Lieu", "Début", "Fin", "Rounds", "Actuel", "En cours", "Description"]
    LARGEURS_COLONNES = [4, 20, 20, 10, 10, 6, 6, 8, 60]

    def __init__(self):
        pass

    def list_tournaments(self, listes_tournois):
        clear_screen()
        print(self.TITRE_VUE)
        self.print_line(self.HEADER, self.LARGEURS_COLONNES)
        print("\n")
        for tournoi in listes_tournois:
            self.print_line(tournoi, self.LARGEURS_COLONNES)
        retour = input("\nSélectionnez un tournoi ou appuyez sur Entrée pour quitter ")
        return retour


class ReportTournamentPlayersView(ListView):

    TITRE_VUE = "LISTE DES JOUEURS DU TOURNOI PAR ORDRE ALPHABETIQUE\n" \
        "---------------------------------------------------\n"

    HEADER = ["Numero", "Nom", "Prenom", "Date naissance", "Club", "N°. participant", "Points"]
    LARGEURS_COLONNES = [15, 20, 20, 14, 7, 15, 6]

    def __init__(self):
        pass

    def print_player_list(self, listes_infos_joueurs):
        clear_screen()
        print(self.TITRE_VUE)
        self.list_joueurs(listes_infos_joueurs)

    def list_joueurs(self, listes_infos_joueurs):
        self.print_line(self.HEADER, self.LARGEURS_COLONNES)
        print("\n")
        for infos_joueurs in listes_infos_joueurs:
            self.print_line(infos_joueurs, self.LARGEURS_COLONNES)
        print("\n")

    def print_info(self, info):
        print(info)


class ReportTournamentRoundsMatchsView:
    TITRE_VUE = "LISTE DES ROUNDS ET MATCHS\n--------------------------\n"

    def __init__(self):
        print(self.TITRE_VUE)

    def print_rounds_matchs(self, liste_infos_rounds):
        indentation = "         "
        espacement = "     "
        for infos_round in liste_infos_rounds:
            print(infos_round[1] + " > " + "Début : " + infos_round[4] + " - " + "Fin : " + infos_round[5])
            for match in infos_round[2]:
                print(indentation + "joueurs : ", str(match.scores_joueurs[0][0]) + " - "
                      + str(match.scores_joueurs[1][0]) + espacement + "scores  : ", str(match.scores_joueurs[0][1])
                      + " - " + str(match.scores_joueurs[1][1]) + espacement + "Terminé : ", match.est_fini)
            print('\n')
        input("Appuyez sur Entrée...")
