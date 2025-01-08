from models.tournament import Tournament
from views.tournament_view import TournamentMenuView, NewTournamentView, ListTournamentsView, TournamentDisplayView
from controllers.tournament_players_selection_controller import TournamentPlayersSelectionController
from utilities import tournaments_manager as tm
from utilities import constantes
from time import sleep
from os import path
from random import shuffle


class TournamentController:

    FICHIER_JOUEURS = constantes.FICHIER_JOUEURS
    FICHIER_TOURNOIS = constantes.FICHIER_TOURNOIS
    ELEMENTS_MENU = ["1/ Créer un nouveau tournoi\n", "2/ Mettre à jour un tournoi\n", "3/ Lister les tournois\n",
                     "4/ Retour\n"]
    RETOUR = 4

    ELEMENTS_MENU_MOD_TOURNOI = ["1/ Modifier la liste des joueurs\n", "2/ gérer les rounds\n", "3/ Retour\n"]
    RETOUR_MENU_MOD_TOURNOI = len(ELEMENTS_MENU)

    def __init__(self):
        self.view = TournamentMenuView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = self.view.input_choice()

        # Nouveau tournoi
        if choix == 1:
            self.create_tournament()

        # Modification de tournoi existant
        if choix == 2:
            view = ListTournamentsView()
            numero_tournoi_selectionne = -1
            tournois = []
            if path.exists(self.FICHIER_TOURNOIS) is True:
                tournois = tm.load_tournaments(self.FICHIER_TOURNOIS)
                if tournois is not None:
                    listes_infos_tournois = []
                    for infos_tournoi in tournois:
                        listes_infos_tournois.append(infos_tournoi.to_list())
                    while numero_tournoi_selectionne == -1:
                        numero_tournoi = view.list_tournaments(listes_infos_tournois, "R")
                        if numero_tournoi != "":
                            try:
                                numero_tournoi_selectionne = int(numero_tournoi)
                            except ValueError:
                                print("Veuillez entrer un nombre !")
                                sleep(2)
            else:
                print("Fichier des tournois non trouvé")
                sleep(2)

            # si un tournoi a été sélectionné, on affiche les données du tournoi et les actions possibles
            if numero_tournoi_selectionne > 0:
                choix_action = 0
                while choix_action == 0:
                    view = TournamentDisplayView(self.ELEMENTS_MENU_MOD_TOURNOI)
                    tournoi = tournois[int(numero_tournoi)-1]
                    infos_joueurs = []
                    for joueur in tournoi.joueurs:
                        infos_joueurs.append(joueur.to_list())
                    view.print_tournament(tournoi.to_list(), infos_joueurs)
                    choix_action = view.input_choice(nocls=True, title=False)

                if choix_action == self.RETOUR_MENU_MOD_TOURNOI:
                    choix = self.RETOUR
                # modification de la liste des joueurs du tournoi
                if choix_action == 1:
                    controlleur = TournamentPlayersSelectionController()
                    controlleur.select_tournament_players(tournoi)

        # Liste les tournois
        if choix == 3:
            view = ListTournamentsView()
            if path.exists(self.FICHIER_TOURNOIS) is True:
                tournois = tm.load_tournaments(self.FICHIER_TOURNOIS)
                if tournois is not None:
                    listes_infos_tournois = []
                    for infos_tournoi in tournois:
                        listes_infos_tournois.append(infos_tournoi.to_list())
                    view.list_tournaments(listes_infos_tournois)
            else:
                print("Fichier des tournois non trouvé")
                sleep(2)

        # Retour
        if choix == self.RETOUR:
            return choix

    def create_tournament(self):
        '''Créé et sauvegarde les informations
        initiales et les joueurs du tournois'''

        tournoi = Tournament()
        # Entree des infos nom, lieu, date debut et date fin,
        # nombre de rounds et description
        next = False
        while next is False:
            view = NewTournamentView()
            datas = view.param_tournament()
            next = self.check_tournament_datas(datas)
        tournoi.nom = datas[0]
        tournoi.lieu = datas[1]
        tournoi.date_debut = datas[2]
        tournoi.date_fin = datas[3]
        # si le nombre de round est > 0 (non vide)
        # on change la valeur par defaut
        if int(datas[4]) > 0:
            tournoi.nombre_de_rounds = int(datas[4])
        tournoi.description = datas[5]

        # sauvegarde du tournoi créé
        tournois = tm.load_tournaments(self.FICHIER_TOURNOIS)
        # si pas de tournois a charger
        if tournois is None:
            tournois = []
            tournoi.set_numero_tournoi(1)
        else:
            tournoi.set_numero_tournoi(len(tournois)+1)
        tournois.append(tournoi)
        tm.save_tournaments(tournois, self.FICHIER_TOURNOIS)
        sleep(2)

    def check_nom(self, nom):
        '''Vérifie si le champ nom est rempli'''
        if nom == "":
            print("Le nom ne peut etre vide !")
            return False
        return True

    def check_lieu(self, lieu):
        '''Vérifie si le champ lieu est rempli'''
        if lieu == "":
            print("Le lieu ne peut etre vide !")
            return False
        return True

    def check_date_debut(self, date_debut):
        longueur = len(date_debut)
        if longueur < 10 or longueur > 10:
            print("Date de début mal formatée !")
            return False
        return True

    def check_date_fin(self, date_fin):
        longueur = len(date_fin)
        if longueur < 10 or longueur > 10:
            print("Date de fin mal formatée !")
            return False
        return True

    def check_nombre_rounds(self, nombre):
        '''Vérifie l'entrée du champ nombre de round
        renvoit 0 si le champ est vie,
        -1 si ce n'est pas un nombre qui a ete entré,
        sinon le nombre de rounds est renvoyé'''
        if nombre == "":
            return 0
        # test si un nombre est bien entre
        try:
            test_nombre = int(nombre)
        except ValueError:
            print("Veuillez entrer un nombre !")
            return -1
        return test_nombre

    def check_tournament_datas(self, tournament_datas):
        '''Vérifie les champs du tournoi'''
        nom = tournament_datas[0]
        lieu = tournament_datas[1]
        date_debut = tournament_datas[2]
        date_fin = tournament_datas[3]
        nombre_de_rounds = tournament_datas[4]
        print("")
        nom_ok = self.check_nom(nom)
        lieu_ok = self.check_lieu(lieu)
        date_debut_ok = self.check_date_debut(date_debut)
        date_fin_ok = self.check_date_fin(date_fin)
        nombre_de_rounds = self.check_nombre_rounds(nombre_de_rounds)
        if (nom_ok and lieu_ok and date_debut_ok and date_fin_ok and nombre_de_rounds > -1):
            return True
        sleep(2)
        return False

    def shuffle_players(self, joueurs):
        '''Melange la liste des joueurs et attribue un numero de joueur pour le tournoi'''
        shuffle(joueurs)
        i = 1
        for joueur in joueurs:
            joueur.numero_en_tournoi = i
            i += 1
        return joueurs
