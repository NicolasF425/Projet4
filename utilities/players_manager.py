# gere la sauvegarde d'une liste de joueurs
# et la lecture du fichier des joueurs
import json
from models.player import Player


@staticmethod
def save_players(players, filename):
    try:
        with open(filename, "w") as file:
            liste_dicts = [player.to_dict() for player in players]
            json.dump(liste_dicts, file, indent=4)
            print(f"Sauvegarde effectuee dans {filename}")
    except Exception as e:
        print(f"Erreur de sauvegarde : {e}")


@staticmethod
def load_players(filename):
    '''Charge une liste de joueurs a partir d'un fichier json'''
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        players = [Player(**d) for d in data]
        return players
    except FileNotFoundError:
        print(f"Fichier {filename} non trouve.")
    except Exception as e:
        print(f"Erreur de chargement: {e}")
    return None


@staticmethod
def export_players(filename, players):
    try:
        with open(filename, "w") as file:
            file.write("Nom" + " " + "Prenom" + " " + "Date de naissance" + " " + "Identifiant club\n")
            for player in players:
                file.write(player.nom + " " + player.prenom + " " + player.date_de_naissance + " "
                           + player.identifiant_club+"\n")
        return True
    except Exception as e:
        print(f"Erreur {e}")
    return None
