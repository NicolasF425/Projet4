class Match:

    def __init__(self, Player1, Player1Score, Player2, Player2Score):
        self.PlayersScores = ([Player1, Player1Score], [Player2, Player2Score])

    def to_dict(self):
        return {
            "joueur_1": self.PlayersScores[0][0].to_dict(),
            "score_joueur_1": self.PlayersScores[0][1],
            "joueur_2": self.PlayersScores[1][0].to_dict(),
            "score_joueur_2": self.PlayersScores[1][1]
        }
