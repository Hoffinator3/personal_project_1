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
        else:
            raise Exception(f"Move has no PP")
        
        stab = self.is_stab(move_index)

        player_attack = self.moves[move_index].calculate_damage(attacker, defender, stab)
        defender.take_damage(player_attack)

        print(f"\033[38;2;136;33;74m[{attacker.name}]\033[0m used {attacker.moves[move_index].get_name()} for \033[38;2;136;33;74m{player_attack} damage\033[0m ({move.pp} PP Remaining).")
        print(f"    {defender.name} \033[38;2;136;33;74mnew hp: {defender.stats["hp"]}\033[0m")

    def is_stab(self, move_index):
        print(f"Is stab? {self.moves[move_index].type == self.types["type1"] or self.moves[move_index].type == self.types["type2"]}")
        return (self.moves[move_index].type == self.types["type1"] or self.moves[move_index].type == self.types["type2"])

    def list_moves(self):
        result = []
        for i in range(len(self.moves)):
            result.append(f"{i+1}. {self.moves[i].get_name()}")
            i += 1
        return result