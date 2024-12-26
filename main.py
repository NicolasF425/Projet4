# from models.player import Player
# from utilities.players_manager import save_players, load_players

from controllers.player_controller import PlayerController as PC
from views.player_view import AddPlayerView, ListPlayersView

'''
player1 = Player(nom="Nom1", prenom="Prenom1", date_de_naissance="12/12/2000",
                 identifiant_club="AB12345")
player2 = Player(nom="Nom2", prenom="Prenom2", date_de_naissance="15/10/2000",
                 identifiant_club="AB12345")

saved_players = [player1, player2]

save_players(saved_players, "joueurs.json")

loaded_players = load_players("joueurs.json")

for player in loaded_players:
    player.print_player()
'''

# view = AddPlayerView()
# view.add_new_player()
view = ListPlayersView()
view.list_players_by_name()
