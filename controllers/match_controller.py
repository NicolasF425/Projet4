from models.match import Match


class MatchController:

    def create_match(self, Player1, Player2, Player1Score, Player2Score):
        match = Match(Player1, Player2, Player1Score, Player2Score)
        return match
