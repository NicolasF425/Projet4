from views.tournament_view import PlayerSelectionView
from utilities import players_manager as pm, tournaments_manager as tm
from time import sleep


class TournamentPlayersSelectionController:

    def __init__(self):
        pass

    def select_tournament_players(self, tournoi):
        '''Gestion de la sélection des joueurs pour un tournoi'''

        view = PlayerSelectionView(tournoi)
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
