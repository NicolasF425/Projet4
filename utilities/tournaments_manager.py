# gere la sauvegarde d'une liste de tournois
# et la lecture du fichier des tournois

import json
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from models.round import Round


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

            # joueurs des tournois
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

            # rounds
            liste_rounds = []
            for i in range(0, len(tournament.rounds)):
                round = Round()
                round.numero = tournament.rounds[i]["numero"]
                round.nom = tournament.rounds[i]["nom"]

                # matchs du round
                liste_matchs = []
                for j in range(0, len(tournament.rounds[i].matchs)):
                    match = Match()
                    numero_joueur1 = tournament.rounds[i].matchs[j].scores_joueurs[0][0]
                    numero_joueur2 = tournament.rounds[i].matchs[j].scores_joueurs[1][0]
                    match.set_players_numbers(numero_joueur1, numero_joueur2)
                    score_joueur1 = tournament.rounds[i].matchs[j].scores_joueurs[0][1]
                    score_joueur2 = tournament.rounds[i].matchs[j].scores_joueurs[1][1]
                    match.set_resultat(score_joueur1, score_joueur2)
                    match.est_fini = tournament.rounds[i].matchs[j].est_fini
                    liste_matchs.append(match)
                round.matchs = liste_matchs

                # joueurs du round
                liste_joueurs = []
                for k in range(0, len(tournament.joueurs)):
                    numero_joueur = tournament.joueurs[k]["numero_joueur"]
                    nom_joueur = tournament.joueurs[k]["nom"]
                    prenom_joueur = tournament.joueurs[k]["prenom"]
                    date_naissance = tournament.joueurs[k]["date_de_naissance"]
                    identifiant_club = tournament.joueurs[k]["identifiant_club"]
                    numero_en_tournoi = tournament.joueurs[k]["numero_en_tournoi"]
                    score = tournament.joueurs[k]["score"]
                    joueur = Player(numero_joueur=numero_joueur, nom=nom_joueur, prenom=prenom_joueur,
                                    date_de_naissance=date_naissance, identifiant_club=identifiant_club,
                                    numero_en_tournoi=numero_en_tournoi, score=score)
                    liste_joueurs.append(joueur)

                round.joueurs = liste_joueurs
                round.date_heure_debut = tournament.rounds[i].date_heure_debut
                round.date_heure_fin = tournament.rounds[i].date_heure_debut
                round.est_fini = tournament.rounds[i].est_fini
                liste_rounds.append(round)
            tournament.rounds = liste_rounds

        return tournaments
    except FileNotFoundError:
        print(f"Fichier {filename} non trouve.")
    except Exception as e:
        print(f"Erreur de chargement: {e}")
    return None
