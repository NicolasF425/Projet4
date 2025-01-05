class Player:
    '''Classe de joueur pour les fichier json'''

    def __init__(self, nom="", prenom="", date_de_naissance="", identifiant_club="", numero_joueur=0,
                 numero_en_tournoi=0, score=0):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.identifiant_club = identifiant_club
        self.numero_joueur = numero_joueur
        self.numero_en_tournoi = numero_en_tournoi
        self.score = score

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
                "identifiant_club": self.identifiant_club,
                "numero_joueur": self.numero_joueur
            }
        else:
            return {
                "nom": self.nom,
                "prenom": self.prenom,
                "date_de_naissance": self.date_de_naissance,
                "identifiant_club": self.identifiant_club,
                "numero_joueur": self.numero_joueur,
                "numero_en_tournoi": self.numero_en_tournoi,
                "score": self.score
            }

    def to_list(self):
        return [self.nom, self.prenom, self.date_de_naissance, self.identifiant_club,
                self.numero_joueur, self.numero_en_tournoi, self.score]
