from models.player import Player


class PlayerController:

    def create_player(self, Name, FirstName, BirthDate, ClubId):
        player = Player(Name, FirstName, BirthDate, ClubId)
        return player
