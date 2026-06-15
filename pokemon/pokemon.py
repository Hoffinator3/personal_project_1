#from moves import Moves

class Pokemon:
    def __init__(self, name: str, level: int, stats: dict, types, moves: list, status_effects):
        self.name = name
        self.level = level
        self.stats = stats
        self.types = types
        self.moves = moves
        self.status_effects = status_effects

    def take_damage(self):
        pass

    def heal(self):
        pass

    def level_up(self):
        pass

    def use_move(self):
        pass

    def is_stab(self):
        pass