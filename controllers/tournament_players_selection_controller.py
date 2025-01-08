from views.tournament_view import PlayerSelectionView
from utilities import players_manager as pm, tournaments_manager as tm
from time import sleep
from utilities import constantes


class TournamentPlayersSelectionController:

    def __init__(self):
        pass

    def select_tournament_players(self, tournoi):
        '''Gestion de la sélection des joueurs pour un tournoi'''

        view = PlayerSelectionView()
        # on charge tous les joueurs du fichier json
        tous_joueurs = pm.load_players(constantes.FICHIER_JOUEURS)
        # on initialise la liste des joueurs selectionnes
        selection_joueurs = []
        # listes pour affichage :
        tous_joueurs_elements = []
        selection_joueurs_elements = []
        # on met a jour la liste des joueurs du tournoi
        for joueur in tournoi.joueurs:
            selection_joueurs.append(joueur)
        # on retire les joueurs du tournoi de la liste generale
        liste_numeros = []
        for joueur in selection_joueurs:
            liste_numeros.append(joueur.numero_joueur)
        for numero in liste_numeros:
            i = 0
            for joueur in tous_joueurs:
                if joueur.numero_joueur == numero:
                    del tous_joueurs[i]
                i += 1
        # on met a jour les listes d'elements a afficher
        for joueur in tous_joueurs:
            tous_joueurs_elements.append(joueur.to_list())
        for joueur in selection_joueurs:
            selection_joueurs_elements.append(joueur.to_list())

        # on sélectionne les joueurs
        selection_ok = False
        while selection_ok is False:
            view.print_vue(tous_joueurs_elements, selection_joueurs_elements)
            numero_choisi = view.select_players()
            # si le numero est vide on termine la selection
            if numero_choisi == "":
                selection_ok = True
            else:
                try:
                    numero_choisi = int(numero_choisi)
                    # on met a jour les listes de joueurs
                    # teste si le numero est dans la liste generale
                    # si oui on le transfere vers la liste des selectionnes
                    next = True
                    i = 0
                    for joueur in tous_joueurs:
                        if joueur.numero_joueur == numero_choisi:
                            joueur = tous_joueurs[i]
                            selection_joueurs.append(joueur)
                            selection_joueurs_elements.append(joueur.to_list())
                            del tous_joueurs[i]
                            del tous_joueurs_elements[i]
                            next = False
                            break
                        i += 1

                    j = 0
                    if next is True:
                        for joueur in selection_joueurs:
                            if joueur.numero_joueur == numero_choisi:
                                tous_joueurs.append(joueur)
                                tous_joueurs_elements.append(joueur.to_list())
                                del selection_joueurs[j]
                                del selection_joueurs_elements[j]
                                break
                            j += 1

                except ValueError:
                    print("Vous devez entrer un numéro !")
                    sleep(2)

        tournoi.joueurs = selection_joueurs
        tournois = tm.load_tournaments(constantes.FICHIER_TOURNOIS)
        if tournois is not None:
            for t in tournois:
                if t.numero_tournoi == tournoi.numero_tournoi:
                    t.joueurs = tournoi.joueurs
            tm.save_tournaments(tournois, constantes.FICHIER_TOURNOIS)
            sleep(2)
