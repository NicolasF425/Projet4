class Match:

    '''Initialise un nouveau match avec les scores à 0'''
    def __init__(self, player1, player2):
        self.players_scores = ([player1, 0],
                               [player2, 0])
        self.is_finished = False

    '''Met a jour le score des joueurs et termine le match'''
    def set_result(self, score_player1, score_player2):
        result = ([self.players_scores[0][0], score_player1],
                  [self.players_scores[1][0], score_player2])
        self.players_scores = result
        self.is_finished = True

    def to_dict(self):
        return {
            "joueur_1": self.players_scores[0][0].to_dict(),
            "score_joueur_1": self.players_scores[0][1],
            "joueur_2": self.players_scores[1][0].to_dict(),
            "score_joueur_2": self.players_scores[1][1]
        }
