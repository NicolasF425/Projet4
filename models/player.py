class Player:
    '''Classe de joueur pour les fichier json'''

    def __init__(self, **kwargs):
        for cle, valeur in kwargs.items():
            setattr(self, cle, valeur)
        self.numero_joueur = 0
        self.score = 0

    def set_player_id(self, id):
        self.numero_joueur = id

    def update_score(self, points):
        self.score += points

    def __repr__(self):
        return f"Player({self.__dict__})"

    def to_dict(self, mode=1):
        if mode == 1:
            return {
                "nom": self.nom,
                "prenom": self.prenom,
                "date_de_naissance": self.date_de_naissance,
                "identifiant_club": self.identifiant_club
            }
        else:
            return {
                "nom": self.nom,
                "prenom": self.prenom,
                "date_de_naissance": self.date_de_naissance,
                "identifiant_club": self.identifiant_club,
                "numero_joueur": self.numero_joueur,
                "score": self.score
            }
