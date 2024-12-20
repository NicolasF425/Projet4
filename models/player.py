class Player:

    def __init__(self, Name, FirstName, BirthDate, ClubId):
        self.Name = Name
        self.FirstName = FirstName
        self.BirthDate = BirthDate
        self.ClubId = ClubId

    def to_dict(self):
        return {
            "nom": self.Name,
            "prenom": self.FirstName,
            "date_de_naissance": self.BirthDate,
            "Identifiant_club": self.ClubId
        }
