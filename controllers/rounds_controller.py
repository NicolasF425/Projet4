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
        shuffle(joueurs)
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

    def update_tournament(self):
        tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
        if tournois is not None:
            numero = self.tournoi.numero_tournoi-1
            tournois[numero] = self.tournoi
            tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)
            sleep(3)
