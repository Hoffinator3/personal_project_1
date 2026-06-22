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
        action = input("> ")
        if action == None or action == "":
            raise Exception(f"invalid action")
        return int(action) - 1

    def trainer_action(self):
        return 0
    
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


    def switch_active_pokemon(self):
        print(f"Please select a team member:")
        team_list = self.trainer_one.list_team()
        team_join = " ".join(team_list)
        print(f'{team_join}')
        action = input("> ")
        if action == None or action == "":
            raise Exception(f"invalid action")
        action = int(action)

        if action <= 0:
            return
        else:
            self.trainer_one.switch_lead(action)

        return int(action) - 1


    def player_choice(self):
        print(f"Please make a choice:")
        print(f"1: Fight    2: Party")

        valid_choices = (1, 2)
        while True:
            action = input("> ")
            action = int(action)
            if action in valid_choices:
                #action = valid_choices[action]
                break
            print("Invalid choice. Please try again.")

        print(f"action = {action}")
        
        #If fight, select a move and return
        if action == 1:
            return self.player_action()
        #If party,
        if action == 2:
            # If no other team member, return choice function
            if len(self.trainer_one.team) == 1:
                print(f"No other pokemon are available.")
                return self.player_choice()
            
            #store current mon
            #used to handle "exiting" the party selection
            current_mon = self.trainer_one.team[0].name
            
            print(f"Please select a team member:")
            team_list = self.trainer_one.list_team()
            team_join = " ".join(team_list)
            print(f'{team_join}')
            team_choice = input("> ")
            if team_choice == None or team_choice == "":
                raise Exception(f"invalid action")
            team_choice = int(team_choice) -1

            if team_choice == 0:
                return self.player_choice()

            if self.trainer_one.team[0].name == current_mon:
                return self.player_choice()
            else:
                return -1
            