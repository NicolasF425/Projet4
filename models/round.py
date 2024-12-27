from models.match import Match


class Round:

    def __init__(self, players):
        self.name = ""
        self.matchs = []
        self.players = players
        self.date_heure_debut = None
        self.date_heure_fin = None

    def set_name(self, name):
        self.name = name

    def add_match(self, match):
        self.matchs.append(match)

    def to_dict(self):
        return {
            "Nom": self.name,
            "matchs": [match.to_dict() for match in self.matchs]
        }

    def init_matches(self):
        '''Creation des paires'''
        number_of_players = len(self.players)
        for n in range(number_of_players, 2):
            match = Match(self.players[n], self.players[n+1])
            self.add_match(match)
