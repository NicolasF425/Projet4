from views.tournament_view import TournamentView, NewTournamentView, PlayerSelectionView
from models.tournament import Tournament
from utilities import players_manager as pm
from utilities import tournaments_manager as tm
from utilities import constantes
from time import sleep
from random import shuffle


class TournamentController:

    FICHIER_JOUEURS = constantes.FICHIER_JOUEURS
    FICHIER_TOURNOIS = constantes.FICHIER_TOURNOIS
    ELEMENTS_MENU = ["1/ Créer un nouveau tournoi\n", "2/ Mettre à jour un tournoi\n", "3/ Lister les tournois\n",
                     "4/ Retour\n"]
    RETOUR = 4

    def __init__(self):
        self.view = TournamentView(self.ELEMENTS_MENU)
        self.view.print_view()

    def manage_input(self):
        choix = self.view.input_choice()

        # Nouveau tournoi
        if choix == 1:
            self.create_tournament()

        # Modification de tournoi existant
        if choix == 2:
            pass

        # Liste des tournois
        if choix == 3:
            pass

        # Retour
        if choix == self.RETOUR:
            return choix

    def create_tournament(self):
        '''Créé et sauvegarde les informations
        initiales et les joueurs du tournois'''

        tournoi = Tournament()
        # Entree des infos nom, lieu, date debut et date fin
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

        # si ok on passe a la selection des joueurs
        view = PlayerSelectionView()
        selection_ok = False
        # on charge tous les joueurs du fichier json
        tous_joueurs = pm.load_players(self.FICHIER_JOUEURS)
        selection_joueurs = []
        tous_joueurs_elements = []
        selection_joueurs_elements = []
        for joueur in tous_joueurs:
            tous_joueurs_elements.append(joueur.to_list())
        while selection_ok is False:
            view.print_vue(tous_joueurs_elements, selection_joueurs_elements)
            numero_choisi = view.select_players()
            # si le numero est vide on termine la sélection
            if numero_choisi == "":
                selection_ok = True
            else:
                next = False
                numero_choisi = int(numero_choisi)
                # on met a jour les listes de joueurs
                # on teste si le numero entré est dans la liste générale
                # puis dans la liste de sélection s'il n'y est pass
                i = 0
                for joueur in tous_joueurs:
                    if joueur.numero_joueur == numero_choisi:
                        joueur = tous_joueurs[i]
                        selection_joueurs.append(joueur)
                        selection_joueurs_elements.append(joueur.to_list())
                        del tous_joueurs[i]
                        del tous_joueurs_elements[i]
                        next = True
                        break
                j = 0
                if next is not True:
                    for joueur in selection_joueurs:
                        if joueur.numero_joueur == numero_choisi:
                            tous_joueurs.append(joueur)
                            del selection_joueurs[j]
                            tous_joueurs_elements.append(joueur.to_list())
                            del selection_joueurs_elements[j]
                            break

        tournoi.joueurs = selection_joueurs
        self.shuffle_players(selection_joueurs)
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
