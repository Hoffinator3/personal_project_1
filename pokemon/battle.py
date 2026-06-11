from pokemon import Pokemon
from moves import Moves
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
        pass