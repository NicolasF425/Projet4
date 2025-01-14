from models.tournament import Tournament
from views.tournament_view import TournamentMenuView, NewTournamentView, ListTournamentsView, TournamentDisplayView
from views.reports_view import ReportTournamentRoundsMatchsView, ReportTournamentPlayersView
from controllers.tournament_players_selection_controller import TournamentPlayersSelectionController
from controllers.rounds_controller import RoundsController
from controllers.tournament_rounds_upate_controller import TournamentRoundsUpdateController
from utilities import tournaments_manager as tm
from utilities import constantes
from time import sleep
from os import path


class TournamentController:
    '''Controlleur pour la création d'un nouveau tournoi'''

    ELEMENTS_MENU = ["1/ Créer un nouveau tournoi\n", "2/ Mettre à jour un tournoi\n", "3/ Lister les tournois\n",
                     "4/ Retour\n"]
    RETOUR = 4

    ELEMENTS_MENU_MOD_TOURNOI = ["1/ Modifier la liste des joueurs\n", "2/ Créer un nouveau round\n",
                                 "3/ Mettre à jour les scores\n", "4/ Retour\n"]
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
            if path.exists(constantes.FICHIER_TOURNOIS) is True:
                tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
                if tournois is not None:
                    listes_infos_tournois = []
                    for infos_tournoi in tournois:
                        listes_infos_tournois.append(infos_tournoi.to_list())
                    while numero_tournoi_selectionne == -1:
                        numero_tournoi = view.list_tournaments(listes_infos_tournois, "R")
                        if numero_tournoi != "":
                            if numero_tournoi == constantes.ESCAPE:
                                break
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

                # dernier choix > retour
                if choix_action == self.RETOUR_MENU_MOD_TOURNOI:
                    choix = self.RETOUR

                # 1> modification de la liste des joueurs du tournoi
                if choix_action == 1:
                    if tournoi.en_cours == "Non":
                        controlleur = TournamentPlayersSelectionController()
                        controlleur.select_tournament_players(tournoi)
                    else:
                        print("Tournoi commencé, modification de la liste des joueurs impossible !")
                        sleep(2)

                # 2> création d'un nouveau round
                if choix_action == 2:
                    # si creation du premier round, lancement du tournoi
                    if tournoi.en_cours == "Non" and tournoi.round_actuel == 1:
                        reponse = input("Initialiser le premier round ? Cela bloquera la liste des joueurs et "
                                        "lancera le tournoi..."
                                        + "\nTapez 'oui' puis appuyez sur Entrée pour valider "
                                        + "ou appuyez sur Entrée pour annuler : ")
                        if reponse == "oui":
                            if len(tournoi.joueurs) > tournoi.nombre_de_rounds:
                                tournoi.en_cours = "Oui"
                                controlleur = RoundsController(tournoi)
                                controlleur.init_round(1)
                            else:
                                print("Pas assez de joueurs !")
                                sleep(2)
                    # sinon creation d'un nouveau round
                    elif tournoi.en_cours == "Oui":
                        reponse = input("Initialiser le prochain round ? "
                                        + "\nTapez 'oui' puis appuyez sur Entrée pour valider "
                                        + "ou appuyez sur Entrée pour annuler : ")
                        if reponse == "oui":
                            controlleur = RoundsController(tournoi)
                            controlleur.init_round(tournoi.round_actuel+1)

                # 3> Mise a jour des rounds et des resultats des matchs
                if choix_action == 3:
                    controlleur = TournamentRoundsUpdateController()
                    controlleur.manage_rounds(tournoi)

        # Liste les tournois
        if choix == 3:
            view = ListTournamentsView()
            if path.exists(constantes.FICHIER_TOURNOIS) is True:
                tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
                if tournois is not None:
                    listes_infos_tournois = []
                    for tournoi in tournois:
                        listes_infos_tournois.append(tournoi.to_list())
                    retour = view.list_tournaments(listes_infos_tournois, retour="R")

                    # si on a choisi un tournoi
                    if retour != "" and retour != constantes.ESCAPE:
                        try:
                            numero_tournoi = int(retour)
                            # on enleve 1 car l'indice commence a 0 et les tournois a 1
                            indice_tournoi = numero_tournoi-1

                            # affichage des joueurs tries par ordre alphabetique
                            joueurs_tournoi = self.sort_by_name(tournois[indice_tournoi].joueurs)
                            listes_infos_joueurs = []
                            for joueur in joueurs_tournoi:
                                infos_joueur = joueur.to_list()
                                listes_infos_joueurs.append(infos_joueur)
                            players_view = ReportTournamentPlayersView()
                            players_view.print_player_list(listes_infos_joueurs)

                            # affichage des rounds et des matchs
                            rounds_view = ReportTournamentRoundsMatchsView()
                            liste_infos_rounds = []
                            for round in tournois[indice_tournoi].rounds:
                                infos_round = round.to_list()
                                liste_infos_rounds.append(infos_round)
                            rounds_view.print_rounds_matchs(liste_infos_rounds)

                        except ValueError:
                            print("Vous devez entrer un nombre !")
                            sleep(2)
                        except Exception as err:
                            print(f"Erreur {err} !")
                            sleep(5)
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
        if next == constantes.ESCAPE:
            return constantes.ESCAPE
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
        tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
        # si pas de tournois a charger
        if tournois is None:
            tournois = []
            tournoi.set_numero_tournoi(1)
        else:
            tournoi.set_numero_tournoi(len(tournois)+1)
        tournois.append(tournoi)
        tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)
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
        if tournament_datas == constantes.ESCAPE:
            return constantes.ESCAPE
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

    def sort_by_name(self, joueurs):
        '''Trie les joueurs par nom et par ordre alphabétique'''
        sorted_players = sorted(joueurs, key=lambda player: player.nom)
        return sorted_players
