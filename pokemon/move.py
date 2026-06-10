
class Move:
    def __init__(self, name: str, power: int, type, pp: int):
        self.name = name
        self.power = power
        self.type = type
        self.pp = pp

    def calculate_damage(self):
        pass

    def can_use(self):
        pass