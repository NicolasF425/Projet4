class Tournament:

    def __init__(self, name, location, start_date, number_of_rounds=4,
                 description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = ""
        self.number_of_rounds = number_of_rounds
        self.round_number = 1
        self.players = []
        self.rounds = []
        self.description = description

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def set_end_date(self, end_date):
        self.end_date = end_date

    def to_dict(self):
        return {
            "nom": self.name,
            "lieu": self.location,
            "date_debut": self.start_date,
            "date_fin": self.end_date,
            "joueurs": [player.to_dict() for player in self.players],
            "tours": [round.to_dict() for round in self.rounds],
            "description": self.description
        }
