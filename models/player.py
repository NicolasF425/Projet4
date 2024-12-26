class Player:

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

    def print_player(self):
        print("Nom : ", self.nom)
        print("Prenom : ", self.prenom)
        print("Date de naissance : ", self.date_de_naissance)
        print("Identifiant du club : ", self.identifiant_club)
