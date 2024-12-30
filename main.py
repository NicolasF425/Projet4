from models.player import Player
from utilities.players_manager import save_players, load_players
from views.player_view import AddPlayerView, ListPlayersView

from models.tournament import Tournament
from models.match import Match
from models.player import TournamentPlayer
from utilities import tournaments_manager as TM


def test_tournament():
    player1 = TournamentPlayer(nom="Nom1", prenom="Prenom1", date_de_naissance="12/12/2000",
                               identifiant_club="AB12345")
    player2 = TournamentPlayer(nom="Nom2", prenom="Prenom2", date_de_naissance="15/10/2000",
                               identifiant_club="AB12345")
    player3 = TournamentPlayer(nom="Nom3", prenom="Prenom3", date_de_naissance="12/12/1990",
                               identifiant_club="AB12345")
    player4 = TournamentPlayer(nom="Nom4", prenom="Prenom4", date_de_naissance="15/10/1996",
                               identifiant_club="AB12345")

    tournament = Tournament("Nom", "Location", "12/11/2025", "13/11/2025", 4, 1, [], [], "Test", [])
    tournament.add_player(player1)
    tournament.add_player(player2)
    tournament.add_player(player3)
    tournament.add_player(player4)
    tournament.init_rounds()
    match1 = Match(player1, player2)
    match1.set_result(1, 0)
    tournament.rounds[0].add_match(match1)

    print(tournament)
    tournaments = []
    tournaments.append(tournament)
    TM.save_tournaments(tournaments, "tournois.json")

    loaded_tounaments = TM.load_tournaments("tournois.json")
    print(loaded_tounaments)


def test_players():
    player1 = Player(nom="Nom1", prenom="Prenom1", date_de_naissance="12/12/2000", identifiant_club="AB12345")
    player2 = Player(nom="Nom2", prenom="Prenom2", date_de_naissance="15/10/2000", identifiant_club="AB12345")

    saved_players = [player1, player2]

    save_players(saved_players, "joueurs.json")

    loaded_players = load_players("joueurs.json")
    print(loaded_players)

    view = AddPlayerView()
    view.add_new_player()
    view = ListPlayersView()
    view.list_players_by_name()


test_players()
test_tournament()
