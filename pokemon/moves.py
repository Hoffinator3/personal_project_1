#from pokemon.pokemon import Pokemon
import os
import json

# moves.json categories
# 0 = status
# 1 = physical
# 2 = special

class Moves:
    def __init__(self, name: str):
        self.name = name
        with open(os.path.abspath("./data/moves.json"), mode='r') as d:
            move = json.load(d)
            self.power = move[name]["power"]
            self.type = move[name]["type"]
            self.pp = move[name]["pp"]
            self.category = move[name]["category"]

    def calculate_damage(self, attacker, defender) -> int:
        if attacker == None or attacker == "":
            attacker = 1
        if defender == None or defender == "":
            defender = 1
        base = ((attacker.level * 2) / 5 + 2)
        if self.category == 0:
            pass
        if self.category == 1:
            base_stats = base * self.power * (attacker.stats["attack"] / defender.stats["defense"])
        if self.category == 2:
            base_stats = base * self.power * (attacker.stats["sp_attack"] / defender.stats["sp_defense"])

        #Missing calculations for random, stab,  type,  burn
        base_damage = (base_stats / 50) + 2
        return int(base_damage)


    def can_use(self):
        pass

    def get_name(self):
        return self.name
