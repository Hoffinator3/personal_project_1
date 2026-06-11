from pokemon.pokemon import Pokemon


class Player:
    def __init__(self, name: str, team: list[Pokemon]):
        self.name = name
        self.team = team