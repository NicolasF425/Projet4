from utilities.clear_screen import clear_screen
from utilities import constantes
from time import sleep


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

    def update_score(self, tournoi):
        ok = "Non"
        while ok == "Non":
            print("Mettre à jour un score (valeurs possible : 1 ou 0.5 ou 0)")
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
            ok = self.check_scores(liste_retour, tournoi)

        return liste_retour

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
        return "Oui"

    def print_info(self, info):
        print(info)
