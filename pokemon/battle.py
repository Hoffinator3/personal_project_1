import random
from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
from trainers.player import Player
from trainers.trainer import Trainer


class Battle:
    def __init__(self, trainer_one: Player, trainer_two: Trainer):
        self.trainer_one = trainer_one
        self.trainer_two = trainer_two

    def turn_order(self):
        if self.trainer_one.team[0].stats["speed"] == self.trainer_two.team[0].stats["speed"]:
            return 1 if random.randint(1, 100) % 2 != 0 else 2
        return 1 if self.trainer_one.team[0].stats["speed"] > self.trainer_two.team[0].stats["speed"] else 2

    def player_pokemon_fainted(self):
        if self.trainer_one.team[0].stats["hp"] <= 0:
            self.trainer_one.team[0].fainted = True
            return True
        return False

    def trainer_pokemon_fainted(self):
        if self.trainer_two.team[0].stats["hp"] <= 0:
            self.trainer_two.team[0].fainted = True
            return True
        return False

    def player_action(self):
        print(f"Please select a move:")
        move_list = self.trainer_one.team[0].list_moves()
        move_join = " ".join(move_list)
        print(f'{move_join}')
        action = input()
        if action == None or action == "":
            raise Exception(f"invalid action")
        #player_attack = self.trainer_one.team[0].moves[int(action) - 1].calculate_damage(self.trainer_one.team[0], trainer.team[0])
        #trainer.team[0].take_damage(player_attack)
        
        #print(f"{self.trainer_two.team[0].name} new hp: {self.trainer_two.team[0].stats["hp"]}")
        return int(action) - 1

    def trainer_action(self):
        return 0
        #trainer_attack = self.trainer_two.team[0].moves[0].calculate_damage(self.trainer_two.team[0], self.trainer_one.team[0])
        #self.trainer_one.team[0].take_damage(trainer_attack)
        #print(f"{self.trainer_one.team[0].name} new hp: {self.trainer_one.team[0].stats["hp"]}")
        #return self.trainer_two.team[0].moves[0].get_name()
    
    def battle_ended(self) -> bool:
        player_team_count = len(self.trainer_one.team)
        player_fainted_count = 0
        trainer_team_count = len(self.trainer_two.team)
        trainer_fainted_count = 0

        for i in range(trainer_team_count):
            pokemon = self.trainer_two.team[i]
            if pokemon.fainted == True:
                trainer_fainted_count += 1
        if trainer_team_count == trainer_fainted_count:
            return True
        
        for i in range(player_team_count):
            pokemon = self.trainer_one.team[i]
            if pokemon.fainted == True:
                player_fainted_count += 1
        if player_team_count == player_fainted_count:
            return True
        
        return False