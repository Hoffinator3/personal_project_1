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
        if self.stats["hp"] <= 0:
            self.stats["hp"] = 0
            self.fainted = True
        return self.stats["hp"]

    def heal(self):
        pass

    def level_up(self):
        pass

    def use_move(self, move_index, attacker, defender):
        move = self.moves[move_index]
        if move.pp > 0:
            move.pp -= 1
            print(f"New PP: {move.pp}")
            return self.moves[move_index].calculate_damage(attacker, defender)
        else:
            raise Exception(f"Move has no PP")

    def is_stab(self):
        pass

    def list_moves(self):
        result = []
        for i in range(len(self.moves)):
            result.append(f"{i+1}. {self.moves[i].get_name()}")
            i += 1
        return result