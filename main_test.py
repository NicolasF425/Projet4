from utilities import tournaments_manager as tm


tournaments = tm.load_tournaments("tournois.json")
tm.save_tournaments(tournaments, "tournaments_out.json")
