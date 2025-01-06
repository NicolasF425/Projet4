class Match:

    '''Initialise un nouveau match avec les scores à 0'''
    def __init__(self, joueur1, joueur2):
        self.scores_joueurs = ([joueur1, 0],
                               [joueur2, 0])
        self.est_fini = False

    '''Met a jour le score des joueurs et termine le match'''
    def set_resultat(self, score_player1, score_player2):
        resultat = ([self.scores_joueurs[0][0], score_player1], [self.scores_joueurs[1][0], score_player2])
        self.scores_joueurs = resultat
        self.est_fini = True

    def to_dict(self):
        return {
            "joueur_1": self.scores_joueurs[0][0].to_dict(),
            "score_joueur_1": self.scores_joueurs[0][1],
            "joueur_2": self.scores_joueurs[1][0].to_dict(),
            "score_joueur_2": self.scores_joueurs[1][1]
        }
