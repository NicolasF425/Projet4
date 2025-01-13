from utilities.clear_screen import clear_screen
from utilities import constantes


class RoundsView:

    TITRE_VUE = "LISTE DES ROUNDS ET MATCHS\n--------------------------\n"

    def __init__(self):
        pass

    def print_rounds_matchs(self, liste_infos_rounds):
        clear_screen()
        print(self.TITRE_VUE)

        indentation = "         "
        espacement = "     "
        for infos_round in liste_infos_rounds:
            print(infos_round[1] + " > " + "Début : " + infos_round[4] + " - " + "Fin : " + infos_round[5])
            i = 1
            for match in infos_round[2]:
                print(indentation + str(i) + " >" + espacement + "joueurs : ", str(match.scores_joueurs[0][0]) + " - "
                      + str(match.scores_joueurs[1][0]) + espacement + "scores  : ", str(match.scores_joueurs[0][1])
                      + " - " + str(match.scores_joueurs[1][1]) + espacement + "Terminé : ", match.est_fini)
                i += 1
            print('\n')

    def update_score(self):
        print("Mettre à jour un score (valeurs possible : 1.0 ou 0.5 ou 0.0)")
        numero_match = input("Numero du match : ")
        if numero_match == constantes.ESCAPE:
            return constantes.ESCAPE
        score_premier_joueur = input("Score premier joueur : ")
        if score_premier_joueur == constantes.ESCAPE:
            return constantes.ESCAPE
        score_second_joueur = input("Score second joueur : ")
        if score_second_joueur == constantes.ESCAPE:
            return constantes.ESCAPE
        liste_retour = [numero_match, score_premier_joueur, score_second_joueur]

        return liste_retour
