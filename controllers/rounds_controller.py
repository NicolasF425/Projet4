from random import shuffle
from datetime import datetime
from models.match import Match
from models.round import Round
from utilities import tournaments_manager as tm
from utilities import constantes
from time import sleep


class RoundsController:

    def __init__(self, tournoi):
        self.tournoi = tournoi

    def init_round1(self):
        '''Tour 1 : on mélange les joueurs et on leur attribue un numero de participant'''
        joueurs = self.tournoi.joueurs
        joueurs = self.shuffle_players(joueurs)
        matchs = self.pair_players_round1(joueurs)
        maintenant = datetime.now()
        date_heure = maintenant.strftime("%d/%m/%Y, %H:%M%S")
        round1 = Round()
        round1.nom = "Round 1"
        round1.joueurs = joueurs
        round1.set_date_heure_debut(date_heure)
        round1.matchs = matchs
        self.tournoi.rounds.append(round1)
        self.update_tournament()

    def pair_players_round1(self, joueurs):
        liste_matchs = []
        nb_joueurs = len(joueurs)
        nb_joueurs_pair = True
        # nb_paires = nb_joueurs/2
        if nb_joueurs_pair % 2 == 1:
            nb_joueurs_pair = False
        for i in range(0, nb_joueurs, 2):
            if (i+1) < nb_joueurs:
                match = Match()
                match.set_players_numbers(joueurs[i].numero_en_tournoi, joueurs[i+1].numero_en_tournoi)
                liste_matchs.append(match)
        return liste_matchs

    def create_other_round(self):
        rounds_crees = len(self.tournoi.rounds)
        if len(self.tournoi.nombre_de_rounds > rounds_crees):
            round = Round()
            round.numero = rounds_crees + 1
            round.nom = "Round "+int(round.numero)
            maintenant = datetime.now()
            date_heure = maintenant.strftime("%d/%m/%Y, %H:%M%S")
            round.date_heure_debut = date_heure

    def pair_players_other_round(self, joueurs):
        # on classe les joueurs par score
        joueurs = self.order_players_by_score(joueurs)
        liste_matchs = []

        # tant qu'il y a des joueurs a appairrer
        while len(joueurs) > 0:
            match = Match()

            j = 1
            while len(joueurs) > 0:
                numero_joueur1 = joueurs[0].numero_en_tournoi
                joueur_suivant = joueurs[j].numero_en_tournoi
                # on verifie si le joueur a deja affronte le joueur suivant dans la liste
                for i in range(1, len(self.tournoi.matchs_matrix[numero_joueur1])):
                    if joueur_suivant == self.tournoi.matchs_matrix[numero_joueur1][j]:
                        j += 1
                    else:
                        # si ce n'est pas le cas :
                        numero_joueur2 = joueur_suivant
                        match.set_players_numbers(numero_joueur1, numero_joueur2)
                        del joueurs[0]
                        del joueurs[j]

            liste_matchs.append(match)
        return liste_matchs

    def order_players_by_score(self, joueurs):
        '''Trie les joueurs par score decroissant'''
        sorted_players = sorted(joueurs, key=lambda player: player.score, reverse=True)
        return sorted_players

    def shuffle_players(self, joueurs):
        '''Melange la liste des joueurs et attribue un numero de joueur pour le tournoi'''
        shuffle(joueurs)
        i = 1
        for joueur in joueurs:
            joueur.numero_en_tournoi = i
            i += 1
        return joueurs

    def update_tournament(self):
        tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
        if tournois is not None:
            numero = self.tournoi.numero_tournoi-1
            tournois[numero] = self.tournoi
            tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)
            sleep(3)
