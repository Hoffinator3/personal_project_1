from pokemon.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, team: list[Pokemon]):
        self.name = name
        self.team = team