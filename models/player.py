class Player:
    '''Classe de joueur de base pour le fichier json'''

    def __init__(self, **kwargs):
        for cle, valeur in kwargs.items():
            setattr(self, cle, valeur)

    def __repr__(self):
        return f"Player({self.__dict__})"

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "identifiant_club": self.identifiant_club
        }


class TournamentPlayer(Player):
    '''Classe pour gerer les joueurs en tournois'''

    def __init__(self, **kwargs):
        for cle, valeur in kwargs.items():
            setattr(self, cle, valeur)
        self.id_joueur = 0
        self.score = 0

    def set_player_id(self, id):
        self.id = id

    def update_score(self, points):
        self.score += points
