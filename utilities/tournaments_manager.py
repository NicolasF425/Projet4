# gere la sauvegarde d'une liste de tournois
# et la lecture du fichier des tournois

import json
from models.tournament import Tournament
from models.player import Player


def save_tournaments(tournaments, filename):
    try:
        with open(filename, "w") as file:
            liste_dicts = [tournament.to_dict() for tournament in tournaments]
            json.dump(liste_dicts, file, indent=4)
            print(f"Sauvegarde effectuee dans {filename}")
    except Exception as e:
        print(f"Erreur de sauvegarde : {e}")


def load_tournaments(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        tournaments = [Tournament(**d) for d in data]
        # conversion des listes de dictionnaires en objets
        for tournament in tournaments:
            liste_joueurs = []
            for i in range(0, len(tournament.joueurs)):
                numero_joueur = tournament.joueurs[i]["numero_joueur"]
                nom_joueur = tournament.joueurs[i]["nom"]
                prenom_joueur = tournament.joueurs[i]["prenom"]
                date_naissance = tournament.joueurs[i]["date_de_naissance"]
                identifiant_club = tournament.joueurs[i]["identifiant_club"]
                numero_en_tournoi = tournament.joueurs[i]["numero_en_tournoi"]
                score = tournament.joueurs[i]["score"]
                joueur = Player(numero_joueur=numero_joueur, nom=nom_joueur, prenom=prenom_joueur,
                                date_de_naissance=date_naissance, identifiant_club=identifiant_club,
                                numero_en_tournoi=numero_en_tournoi, score=score)
                liste_joueurs.append(joueur)
            tournament.joueurs = liste_joueurs
        return tournaments
    except FileNotFoundError:
        print(f"Fichier {filename} non trouve.")
    except Exception as e:
        print(f"Erreur de chargement: {e}")
    return None
