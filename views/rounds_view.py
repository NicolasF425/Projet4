from utilities.clear_screen import clear_screen


class RoundsView:

    TITRE_VUE = "LISTE DES ROUNDS ET MATCHS\n--------------------------\n"

    def __init__(self):
        clear_screen()
        print(self.TITRE_VUE)

    def print_rounds_matchs(self, liste_infos_rounds):
        indentation = "         "
        espacement = "     "
        for infos_round in liste_infos_rounds:
            print(infos_round[1] + " > " + "Débuté : " + infos_round[4] + " - " + "Terminé : " + infos_round[6])
            for match in infos_round[2]:
                print(indentation + "joueurs : ", str(match.scores_joueurs[0][0]) + " - "
                      + str(match.scores_joueurs[1][0]) + espacement + "scores  : ", str(match.scores_joueurs[0][1])
                      + " - " + str(match.scores_joueurs[1][1]) + espacement + "Terminé : ", match.est_fini)
            print('\n')
        input("Appuyez sur Entrée...")


class ScoreUpdateView:

    def __init__(self, round):
        self.round = round

    def update_score(self):
        print("Mettre à jour un score (valeurs possible : 1 ou 0.5 ou 0)")
        input("Numero du match : ")
        input("Score joueur 1 : ")
        input("Score joueur 2 : ")
