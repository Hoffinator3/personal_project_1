from pokemon.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, team: list[Pokemon]):
        self.name = name
        self.team = team

    def switch_lead(self, new_lead_index):
        self.team[0], self.team[new_lead_index] = self.team[new_lead_index], self.team[0]