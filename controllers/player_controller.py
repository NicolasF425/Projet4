from time import sleep
from os import path
from models.player import Player
from views.player_view import PlayerView, AddPlayerView, ListPlayersView
from utilities import players_manager as pm
from utilities import constantes


class PlayerController:

    FICHIER_JOUEURS = constantes.FICHIER_JOUEURS
    ELEMENTS_MENU = ["1/ Créer un nouveau joueur\n", "2/ lister les joueurs\n", "3/ Retour\n"]
    RETOUR = len(ELEMENTS_MENU)

    def __init__(self):
        self.view = PlayerView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = self.view.input_choice()

        # Nouveau joueur
        if choix == 1:
            ok = False
            while ok is False:
                view = AddPlayerView()
                player_datas = view.add_new_player()
                ok = self.check_player_datas(player_datas)
            self.create_player(player_datas[0], player_datas[1], player_datas[2], player_datas[3])

        # Liste des joueurs par ordre alphabetique
        if choix == 2:
            view = ListPlayersView()
            joueurs = pm.load_players(self.FICHIER_JOUEURS)
            if joueurs is not None:
                joueurs = self.sort_by_name(joueurs)
                listes_joueurs = []
                for joueur in joueurs:
                    listes_joueurs.append(joueur.to_list())
                view.list_players(listes_joueurs)
            input("\nAppuyez sur entrée...")

        # Retour
        if choix == self.RETOUR:
            return choix

    def create_player(self, Name, FirstName, BirthDate, ClubId):
        '''Sauve la liste des joueurs dans le fichier json'''
        try:
            player = Player(nom=Name, prenom=FirstName,
                            date_de_naissance=BirthDate,
                            identifiant_club=ClubId)
            # on recupere la liste des joueurs du fichier
            players = []
            prochain_numero = 1
            if path.exists(self.FICHIER_JOUEURS) is True:
                players = pm.load_players(self.FICHIER_JOUEURS)
                prochain_numero = len(players) + 1
            # on ajoute le nouveau joueur a la liste
            player.numero_joueur = prochain_numero
            players.append(player)
            # on met a jour le fichier des joueurs
            pm.save_players(players, self.FICHIER_JOUEURS)
            sleep(2)
        except Exception as e:
            print(f"Erreur de fichier : {e}")

    def list_players(self):
        try:
            if path.exists(self.FICHIER_JOUEURS) is True:
                players = pm.load_players(self.FICHIER_JOUEURS)
                return players
        except Exception as e:
            print(f"Erreur de recuperation des joueurs : {e}")
            return None

    def check_nom(self, nom):
        if nom == "":
            print("Le nom ne peut etre vide !")
            return False
        return True

    def check_prenom(self, prenom):
        if prenom == "":
            print("le prenom ne peut etre vide !")
            return False
        return True

    def check_date_de_naissance(self, date_de_naissance):
        longueur = len(date_de_naissance)
        if longueur < 10 or longueur > 10:
            print("date de naissance mal formatée !")
            return False
        return True

    def check_identifiant_club(self, identifiant_club):
        longueur = len(identifiant_club)
        if longueur < 7 or longueur > 7:
            print("Identifiant du club mal formaté !")
            return False
        return True

    # controle si les informations entrees sont celles attendues
    def check_player_datas(self, player_datas):
        nom = player_datas[0]
        prenom = player_datas[1]
        date_de_naissance = player_datas[2]
        identifiant_club = player_datas[3]
        print("")
        nom_ok = self.check_nom(nom)
        prenom_ok = self.check_prenom(prenom)
        date_de_naissance_ok = self.check_date_de_naissance(date_de_naissance)
        identifiant_club_ok = self.check_identifiant_club(identifiant_club)
        if (nom_ok and prenom_ok and date_de_naissance_ok and identifiant_club_ok):
            return True
        sleep(2)
        return False

    def sort_by_name(self, players):
        '''Trie les joueurs par nom et par ordre alphabétique'''
        sorted_players = sorted(players, key=lambda player: player.nom)
        return sorted_players
