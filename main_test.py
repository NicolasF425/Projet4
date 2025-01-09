from utilities import tournaments_manager as tm
from utilities import constantes


tournaments = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
print(tournaments)
