#from pokemon.moves import Moves

class Pokemon:
    def __init__(self, name: str, level: int, stats: dict, types, moves: list, status_effects, fainted=False):
        self.name = name
        self.level = level
        self.stats = stats
        self.types = types
        self.moves = moves
        self.status_effects = status_effects
        self.fainted = fainted

    def take_damage(self, damage):
        self.stats["hp"] -= damage
        return self.stats["hp"]

    def heal(self):
        pass

    def level_up(self):
        pass

    def use_move(self, name):
        for i in range(len(self.moves)-1):
            if self.moves[i].name == name:
                return self.moves[i].name
        raise Exception(f"Pokemon does not know move {name}")

    def is_stab(self):
        pass