from pokemon.pokemon import Pokemon


# moves.json categories
# 0 = status
# 1 = physical
# 2 = special

class Moves:
    def __init__(self, name: str, power: int, type, pp: int, category: int, offense: Pokemon, defense: Pokemon):
        self.name = name
        self.power = power
        self.type = type
        self.pp = pp
        self.category = category
        self.a = offense
        self.d = defense

    def calculate_damage(self):
        base = ((self.pokemon.level * 2) / 5 + 2)
        if self.category == 0:
            pass
        if self.category == 1:
            base_stats = base * self.power * (self.a.stats["attack"] / self.d.stats["defense"])
        if self.category == 2:
            base_stats = base * self.power * (self.a.stats["sp_attack"] / self.d.stats["sp_defense"])

        base_damage = (base_stats / 50) + 2

    def can_use(self):
        pass
