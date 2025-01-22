from time import sleep
from os import path
from models.player import Player
from views.player_view import PlayerMenuView, AddPlayerView, ListPlayersView
from utilities import players_manager as pm
from utilities import constantes


class PlayerController:
    '''Gestion du menu principal des joueurs'''

    FICHIER_JOUEURS = constantes.FICHIER_JOUEURS
    ELEMENTS_MENU = ["1/ Créer un nouveau joueur\n", "2/ lister les joueurs\n", "3/ Retour\n"]
    RETOUR = len(ELEMENTS_MENU)

    def __init__(self):
        self.view = PlayerMenuView(self.ELEMENTS_MENU)
        self.view.print_view()
        self.manage_input()

    def manage_input(self):
        choix = self.view.input_choice()

        # Nouveau joueur
        if choix == 1:
            while True:
                view = AddPlayerView()
                player_datas = view.add_new_player()
                if player_datas == constantes.ESCAPE:
                    break
                if player_datas != constantes.ESCAPE:
                    self.create_player(player_datas[0], player_datas[1], player_datas[2], player_datas[3])
                    break

        # Liste des joueurs par ordre alphabetique
        if choix == 2:
            view = ListPlayersView()
            if path.exists(self.FICHIER_JOUEURS) is True:
                joueurs = pm.load_players(self.FICHIER_JOUEURS)
                if joueurs is not None:
                    joueurs = self.sort_by_name(joueurs)
                    listes_infos_joueurs = []
                    for joueur in joueurs:
                        listes_infos_joueurs.append(joueur.to_list())
                    view.list_players(listes_infos_joueurs)
            else:
                view.print_info("Fichier des joueurs non trouvé")
                sleep(2)

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

    def sort_by_name(self, players):
        '''Trie les joueurs par nom et par ordre alphabétique
        parametre : une liste de Player
        retour : une liste de Player classée'''
        sorted_players = sorted(players, key=lambda player: player.nom)
        return sorted_players
