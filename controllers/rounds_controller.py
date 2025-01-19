from random import shuffle
from datetime import datetime
from models.match import Match
from models.round import Round
from utilities import tournaments_manager as tm
from utilities import constantes


class RoundsController:

    def __init__(self, tournoi):
        self.tournoi = tournoi

    def init_round(self, numero_round):
        '''Tour 1 : on mélange les joueurs et on leur attribue un numero de participant'''
        joueurs_round = self.tournoi.joueurs

        # si premier round
        if numero_round == 1:
            # melange les joueurs
            joueurs_round = self.shuffle_players(joueurs_round)
            # initialisation de la matrice des joueurs deja affrontes
            liste_de_listes = []
            for joueur in joueurs_round:
                liste = []
                liste.append(joueur.numero_en_tournoi)
                liste_de_listes.append(liste)
            self.tournoi.matchs_matrix = liste_de_listes
            matchs = self.pair_players_round1(joueurs_round)

        # si round 2 ou plus
        if numero_round > 1 and numero_round <= self.tournoi.nombre_de_rounds:
            # ordonne les joueurs par scores decroissant
            joueurs_round = self.order_players_by_score(joueurs_round)
            matchs = self.pair_players_other_round(joueurs_round)

        round = Round()
        round.numero = numero_round
        round.nom = "Round " + str(numero_round)
        round.joueurs = joueurs_round
        maintenant = datetime.now()
        date_heure = maintenant.strftime("%d/%m/%Y, %H:%M")
        round.set_date_heure_debut(date_heure)
        round.matchs = matchs
        self.tournoi.rounds.append(round)
        self.tournoi.round_actuel = numero_round
        self.tournoi.en_cours = "Oui"

        # enregistre les modifications
        self.update_tournament()

    def pair_players_round1(self, joueurs_round):
        '''Appairage pour le premier round'''
        liste_matchs = []

        # nombre de joueurs
        nombre_de_joueurs = len(joueurs_round)
        # parite du nombre de joueurs
        nb_joueurs_pair = True
        nb_paires = int(nombre_de_joueurs/2)
        if nombre_de_joueurs % 2 == 1:
            nb_joueurs_pair = False

        appairage_ok = False
        i = 0
        while appairage_ok is not True:
            match = Match()

            numero_joueur1 = joueurs_round[i].numero_en_tournoi
            numero_joueur2 = joueurs_round[i+1].numero_en_tournoi

            # on met a jour la matrice des affrontements
            self.tournoi.matchs_matrix[numero_joueur1-1].append(numero_joueur2)
            self.tournoi.matchs_matrix[numero_joueur2-1].append(numero_joueur1)

            # on affecte les 2 joueurs au match
            match.set_players_numbers(numero_joueur1, numero_joueur2)

            # si tous les appairages sont faits on stop
            i += 2
            if i >= nb_paires*2:
                appairage_ok = True

            # on ajoute le match a la liste
            liste_matchs.append(match)

        # si nombre de joueurs impair le joueur restant obtient 1 point
        if nb_joueurs_pair is not True:
            numero_dernier_joueur = joueurs_round[0].numero_en_tournoi
            self.tournoi.joueurs[numero_dernier_joueur-1].score += 1
            # on considere qu'il a battu un hypothetique joueur 0
            self.tournoi.matchs_matrix[numero_dernier_joueur-1].append(0)

        # on renvoi la liste des matchs
        return liste_matchs

    def pair_players_other_round(self, joueurs_round):
        '''Appairage round 2 et supérieur'''
        liste_matchs = []

        nombre_de_joueurs = len(joueurs_round)
        nb_joueurs_pair = True
        nb_paires = int(nombre_de_joueurs/2)
        if nombre_de_joueurs % 2 == 1:
            nb_joueurs_pair = False

        liste_numeros_joueurs = []
        for joueur in joueurs_round:
            liste_numeros_joueurs.append(joueur.numero_en_tournoi)

        paires = 0
        while paires < nb_paires:
            suivant_ok = False
            suivant = 1
            while suivant_ok is False:
                numero_joueur1 = liste_numeros_joueurs[0]
                joueur_suivant = liste_numeros_joueurs[suivant]

                # on verifie si le joueur a deja affronte le joueur suivant dans la liste
                suivant_ok = True
                for i in range(1, len(self.tournoi.matchs_matrix[numero_joueur1-1])):
                    # si on le trouve on va tester le joueur suivant:
                    if joueur_suivant == self.tournoi.matchs_matrix[numero_joueur1-1][i]:
                        suivant_ok = False
                        suivant += 1
                        break

            # s'il n'a pas affronté le joueur suivant dans la liste des joueurs du round
            if suivant_ok is True:
                numero_joueur2 = joueur_suivant
                match = Match()
                match.set_players_numbers(numero_joueur1, numero_joueur2)
                # on met a jour la matrice des affrontements
                self.tournoi.matchs_matrix[numero_joueur1-1].append(numero_joueur2)
                self.tournoi.matchs_matrix[numero_joueur2-1].append(numero_joueur1)
                del liste_numeros_joueurs[0]
                del liste_numeros_joueurs[suivant-1]
                paires += 1

                liste_matchs.append(match)

        # si nombre de joueurs impair le joueur restant obtient 1 point
        if nb_joueurs_pair is not True:
            numero_dernier_joueur = joueurs_round[0].numero_en_tournoi
            self.tournoi.joueurs[numero_dernier_joueur-1].score += 1
            # on considere qu'il a battu un hypothetique joueur 0
            self.tournoi.matchs_matrix[numero_dernier_joueur-1].append(0)

        return liste_matchs

    def shuffle_players(self, joueurs_round):
        '''Melange la liste des joueurs et attribue un numero de joueur pour le tournoi'''
        shuffle(joueurs_round)
        i = 1
        for joueur in joueurs_round:
            joueur.numero_en_tournoi = i
            i += 1
        return joueurs_round

    def order_players_by_score(self, joueurs):
        '''Trie les joueurs par score decroissant'''
        sorted_players = sorted(joueurs, key=lambda player: player.score, reverse=True)
        return sorted_players

    def update_tournament(self):
        '''Met a jour le fichier des tournois'''
        tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
        if tournois is not None:
            numero = self.tournoi.numero_tournoi-1
            tournois[numero] = self.tournoi
            tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)
