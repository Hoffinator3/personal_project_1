from pokemon.moves import Moves

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

    def use_move(self, move, attacker, defender):
        return self.moves[move].calculate_damage(attacker, defender)

    def is_stab(self):
        pass

    def list_moves(self):
        result = []
        for move in self.moves:
            i = 1
            result.append(f"{i}. {move.get_name()}")
            i += 1
        return result