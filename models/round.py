from models.match import Match


class Round:

    def __init__(self, joueurs):
        self.numero = 1
        self.nom = ""
        self.matchs = []
        self.joueurs = joueurs
        self.date_heure_debut = ""
        self.date_heure_fin = ""
        self.est_fini = "False"

    def set_name(self, name):
        self.nom = name

    def set_date_heure_debut(self, date_heure_debut):
        self.date_heure_debut = date_heure_debut

    def set_date_heure_fin(self, date_heure_fin):
        self.date_heure_fin = date_heure_fin

    def add_match(self, match):
        self.matchs.append(match)

    def to_dict(self):
        return {
            "Numero": self.numero,
            "Nom": self.nom,
            "matchs": [match.to_dict() for match in self.matchs],
            "joueurs": [player.to_dict() for player in self.joueurs],
            "date_heure_debut": self.date_heure_debut,
            "date_heure_fin": self.date_heure_fin,
            "est_fini": self.est_fini
        }

    def check_all_matchs_finished(self):
        matchs_finis = True
        for match in self.matchs:
            if match.is_finished is False:
                matchs_finis = False
                break
        return matchs_finis

    def init_matches(self):
        '''Creation des paires'''
        number_of_players = len(self.joueurs)
        for n in range(number_of_players, 2):
            match = Match(self.joueurs[n], self.joueurs[n+1])
            self.add_match(match)
