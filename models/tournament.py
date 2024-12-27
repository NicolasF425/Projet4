from random import shuffle
from models.round import Round


class Tournament:

    def __init__(self, name, location, start_date, number_of_rounds=4,
                 description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = None  # default value
        self.number_of_rounds = number_of_rounds
        self.round_number = 1
        self.players = []
        self.rounds = []
        self.description = description
        self.matchs_matrix = []     # pour les joueurs deja affrontes

    def __repr__(self):
        return f"Tournament({self.__dict__})"

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

    def init_players_ids(self):
        i = 1
        for player in self.players:
            player.set_player_id(i)
            i += 1

    '''Melange la liste des joueurs'''
    def shuffle_players(self):
        shuffle(self.players)

    '''Initialise la liste des rounds'''
    def set_rounds(self):
        '''On melange les joueurs'''
        self.shuffle_players()
        '''On leur attribue un numero'''
        id = 1
        for player in self.players:
            player.set_player_id(id)
            id += 1
        '''On cree les rounds'''
        for i in range(self.number_of_rounds):
            round = Round(self.players)
            round.set_name("Round" + str(i))
            self.add_round(round)

    def sort_players_by_score(self):
        self.players = self.players.sort(key=lambda player: player.nom)

    def init_matchs_matrix(self):
        for player in self.players:
            self.matchs_matrix.append([player.id])
