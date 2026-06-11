# moves.json categories
# 0 = status
# 1 = physical
# 2 = special

class Moves:
    def __init__(self, name: str, power: int, type, pp: int):
        self.name = name
        self.power = power
        self.type = type
        self.pp = pp

    def calculate_damage(self):
        pass

    def can_use(self):
        pass
