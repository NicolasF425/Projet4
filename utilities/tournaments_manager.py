# gere la sauvegarde d'une liste de tournois
# et la lecture du fichier des tournois

import json
from models.tournament import Tournament


@staticmethod
def save_tournaments(tournaments, filename):
    try:
        with open(filename, "w") as file:
            liste_dicts = [tournament.to_dict() for tournament in tournaments]
            json.dump(liste_dicts, file, indent=4)
            print(f"Sauvegarde effectuee dans {filename}")
    except Exception as e:
        print(f"Erreur de sauvegarde : {e}")


@staticmethod
def load_tournaments(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        tournaments = [Tournament(**d) for d in data]
        return tournaments
    except FileNotFoundError:
        print(f"Fichier {filename} non trouve.")
    except Exception as e:
        print(f"Erreur de chargement: {e}")
    return None
