from random import shuffle
from datetime import datetime
from models.match import Match


class RoundsController:

    def __init__(self, tournoi):
        self.tournoi = tournoi

    def init_round1(self, tournoi):
        '''Tour 1 : on mélange les joueurs et on leur attribue un numero de participant'''
        joueurs = tournoi.joueurs
        joueurs = shuffle(joueurs)
        self.pair_players_round1(joueurs)
        maintenant = datetime.now()
        date_heure = maintenant.strftime("%d/%m/%Y, %H:%M%S")
        tournoi.rounds[0].set_name("Round 1")
        tournoi.rounds[0].date_heure_debut = date_heure

    def pair_players_round1(self, joueurs):
        liste_matchs = []
        nb_joueurs = len(joueurs)
        nb_joueurs_pair = True
        # nb_paires = nb_joueurs/2
        if nb_joueurs_pair % 2 == 1:
            nb_joueurs_pair = False
        for i in range(0, nb_joueurs, 2):
            if (i+1) < nb_joueurs:
                match = Match(joueurs[i], joueurs[i+1])
                liste_matchs.append(match)

    def set_scores(self, match):
        pass

    def shuffle_players(self, joueurs):
        '''Melange la liste des joueurs et attribue un numero de joueur pour le tournoi'''
        shuffle(joueurs)
        i = 1
        for joueur in joueurs:
            joueur.numero_en_tournoi = i
            i += 1
        return joueurs
