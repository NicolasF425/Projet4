from models.player import Player
from models.match import Match

from utilities.JSONfilesManager import to_file


player1 = Player("Nom1", "Prenom1", "12/12/2000", "AB12345")
player2 = Player("Nom2", "Prenom2", "15/10/2000", "AB12345")

match = Match(player1, 1, player2, 0)


to_file(match, "c:\\dev\\programmes\\Projet4\\match.json")
