class Round:

    def __init__(self):
        self.numero = 1
        self.nom = ""
        self.matchs = []
        self.joueurs = []
        self.date_heure_debut = ""
        self.date_heure_fin = ""
        self.est_fini = "Non"

    def __repr__(self):
        return f"Round({self.__dict__})"

    def set_date_heure_debut(self, date_heure_debut):
        self.date_heure_debut = date_heure_debut

    def set_date_heure_fin(self, date_heure_fin):
        self.date_heure_fin = date_heure_fin

    def to_dict(self):
        return {
            "numero": self.numero,
            "nom": self.nom,
            "matchs": [match.to_dict() for match in self.matchs],
            "joueurs": [player.to_dict() for player in self.joueurs],
            "date_heure_debut": self.date_heure_debut,
            "date_heure_fin": self.date_heure_fin,
            "est_fini": self.est_fini
        }

    def to_list(self):
        return [self.numero, self.nom, self.matchs, self.joueurs, self.date_heure_debut, self.date_heure_fin,
                self.est_fini]
