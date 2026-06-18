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

    def use_move(self, move, attacker, defender):
        #move_name = self.moves[move].get_name()
        #print(f"move_name = {move_name}")
        #self.moves[move].get(move_name)["pp"] -= 1
        print(f"self.moves = {self.moves[move].get_name()}")
        return self.moves[move].calculate_damage(attacker, defender)

    def is_stab(self):
        pass

    def list_moves(self):
        result = []
        for i in range(len(self.moves)):
            result.append(f"{i+1}. {self.moves[i].get_name()}")
            i += 1
        return result