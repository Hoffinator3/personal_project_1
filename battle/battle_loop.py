import sys
import json
import os
from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
from pokemon.battle import Battle
from trainers.player import Player
from trainers.trainer import Trainer

def battle_loop(player, rival):
    battle = Battle(player, rival)
    
    while battle.battle_ended() == False:
        # get actions to be performed during the loop
        player_action_selection = battle.player_action()
        trainer_action = battle.trainer_action()

        # get the turn order of the pokemon
        # returns 1 for player, 2 for other trainer
        turn_order = battle.turn_order()
        print(f"turn order: {turn_order}")
        match(turn_order):
            case 1:
                battle.trainer_one.team[0].use_move(player_action_selection, battle.trainer_one.team[0], battle.trainer_two.team[0])
                if battle.trainer_pokemon_fainted():
                    return "WIN!"
                battle.trainer_two.team[0].use_move(trainer_action, battle.trainer_two.team[0], battle.trainer_one.team[0])
                if battle.player_pokemon_fainted():
                    return "LOST!"
            case 2:
                battle.trainer_two.team[0].use_move(trainer_action, battle.trainer_two.team[0], battle.trainer_one.team[0])
                if battle.player_pokemon_fainted():
                    return "LOST!"
                battle.trainer_one.team[0].use_move(player_action_selection, battle.trainer_one.team[0], battle.trainer_two.team[0])
                if battle.trainer_pokemon_fainted():
                    return "WIN!"

        
        #battle.process_move(player_action_selection, trainer_action)
