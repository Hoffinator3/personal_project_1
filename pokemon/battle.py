from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
from trainers.player import Player
from trainers.trainer import Trainer


class Battle:
    def __init__(self, trainer_one: Player, trainer_two: Trainer):
        self.trainer_one = trainer_one
        self.trainer_two = trainer_two

    def turn_order(self):
        if self.trainer_one.team[0].stats["speed"] > self.trainer_two.team[0].stats["speed"]:
            return 1
        else:
            return 2

    def process_move(self):
        match(self.turn_order()):
            case 1:
                self.trainer_one.team[0].use_move().calcuate_damage(self.trainer_one.team[0], self.trainer_two.team[0])
                self.trainer_pokemon_fainted()
                self.trainer_two.team[0].use_move().calcuate_damage(self.trainer_two.team[0], self.trainer_one.team[0])
                self.player_pokemon_fainted()
            case 2:
                self.trainer_two.team[0].use_move().calcuate_damage(self.trainer_two.team[0], self.trainer_one.team[0])
                self.player_pokemon_fainted()
                self.trainer_one.team[0].use_move().calcuate_damage(self.trainer_one.team[0], self.trainer_two.team[0])
                self.trainer_pokemon_fainted()

    def player_pokemon_fainted(self):
        if self.trainer_one.team[0].stats["hp"] <= 0:
            self.trainer_one.team[0].fainted = True

    def trainer_pokemon_fainted(self):
        if self.trainer_one.team[0].stats["hp"] <= 0:
            self.trainer_one.team[0].fainted = True