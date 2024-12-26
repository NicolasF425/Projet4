class Round:

    def __init__(self):
        self.name = ""
        self.matchs = []

    def set_name(self, name):
        self.name = name

    def add_match(self, match):
        self.matchs.append(match)

    def to_dict(self):
        return {
            "matchs": [match.to_dict() for match in self.matchs]
        }
