from models.match import Match


class Tournament:

    def __init__(self, nom="", lieu="", date_debut="", date_fin="", nombre_de_rounds=4, round_actuel=1, joueurs=[],
                 tours=[], description="", matrice_des_matchs=[], en_cours="Non", numero_tournoi=0):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_de_rounds = nombre_de_rounds
        self.round_actuel = round_actuel
        self.joueurs = joueurs
        self.rounds = tours
        self.description = description
        self.matchs_matrix = matrice_des_matchs     # pour les joueurs deja affrontes
        self.en_cours = en_cours
        self.numero_tournoi = numero_tournoi

    def __repr__(self):
        return f"Tournament({self.__dict__})"

    def add_player(self, player):
        self.joueurs.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def set_current_round(self, numero_round):
        self.round_actuel = numero_round

    def check_all_rounds_finished():
        pass

    def set_numero_tournoi(self, numero):
        self.numero_tournoi = numero

    def to_dict(self):
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "nombre_de_rounds": self.nombre_de_rounds,
            "round_actuel": self.round_actuel,
            "joueurs": [joueur.to_dict() for joueur in self.joueurs],
            "tours": [round.to_dict() for round in self.rounds],
            "description": self.description,
            "matrice_des_matchs": self.matchs_matrix,
            "en_cours": self.en_cours,
            "numero_tournoi": self.numero_tournoi
        }

    def to_list(self):
        return [self.numero_tournoi, self.nom, self.lieu, self.date_debut, self.date_fin,
                self.nombre_de_rounds, self.round_actuel, self.en_cours, self.description]

    def players_to_list(self):
        liste_joueurs = []
        for joueur in self.joueurs:
            datas_joueur = joueur.to_list()
            liste_joueurs.append(datas_joueur)
        return liste_joueurs

    def sort_players_by_score(self):
        self.joueurs = self.joueurs.sort(key=lambda player: player.nom)

    def create_match(self, Player1, Player2, Player1Score, Player2Score):
        match = Match(Player1, Player2, Player1Score, Player2Score)
        return match
