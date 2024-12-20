class Round:

    def __init__(self):
        self.matchs = []

    def add_match(self, match):
        self.matchs.append(match)

    def to_dict(self):
        return {
            "matchs": [match.to_dict() for match in self.matchs]
        }
