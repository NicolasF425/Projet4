class Match:

    def __init__(self, player1, player1_score, player2, player2_score):
        self.PlayersScores = ([player1, player1_score],
                              [player2, player2_score])

    def to_dict(self):
        return {
            "joueur_1": self.PlayersScores[0][0].to_dict(),
            "score_joueur_1": self.PlayersScores[0][1],
            "joueur_2": self.PlayersScores[1][0].to_dict(),
            "score_joueur_2": self.PlayersScores[1][1]
        }
