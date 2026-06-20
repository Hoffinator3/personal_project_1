import sys
import json
import os
from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
from pokemon.battle import Battle
from trainers.player import Player
from trainers.trainer import Trainer
from battle.battle_loop import battle_loop


def test_battle():
    b = None
    s = None
    with open(os.path.abspath("./data/pokemon.json"), mode='r') as d:
        pokemon = json.load(d)
        b = Pokemon("Bulbasaur", 5, pokemon["bulbasaur"]["stats"], pokemon["bulbasaur"]["type"], [Moves("tackle")], None)
        s = Pokemon("Squirtle", 5, pokemon["squirtle"]["stats"], pokemon["squirtle"]["type"], [Moves("tackle")], None)

    s.moves[0].calculate_damage(s, b)

    bulb_hp = pokemon["bulbasaur"]["stats"]["hp"]
    b.take_damage(s.moves[0].calculate_damage(s, b))

def test_battle():
    b = None
    s = None
    with open(os.path.abspath("./data/pokemon.json"), mode='r') as d:
        pokemon = json.load(d)
        b = Pokemon("Bulbasaur", 5, pokemon["bulbasaur"]["stats"], pokemon["bulbasaur"]["type"], [Moves("tackle")], None)
        s = Pokemon("Squirtle", 5, pokemon["squirtle"]["stats"], pokemon["squirtle"]["type"], [Moves("tackle")], None) 

    player = Player("zach", [b])
    rival = Trainer("Red", [s])
    fight = Battle(player, rival)
    action = fight.player_action(rival)
    print(f"action = {action}")
    player_attack = action - 1
    fight.trainer_two.team[0].take_damage(player_attack)
    print(f"rival pokemon took {action} damage")
    print(f"{fight.trainer_two.team[0].name} new hp: {fight.trainer_two.team[0].stats["hp"]}")


    trainer_action = fight.trainer_action()
    print(f"trainer uses {trainer_action}")

def test_move():
    path_pokemon_data = "./data/pokemon.json"
    squirt = make_mon(path_pokemon_data, "squirt")
    pidg = make_mon(path_pokemon_data, "pidg")
    
    squirt.use_move(0, squirt, pidg)
    pidg.use_move(0, pidg, squirt)

def make_mon(path, mon):
        with open(os.path.abspath(path), mode='r') as d:
            pokemon = json.load(d)
            if mon == "squirt":
                return Pokemon("Squirtle", 5, pokemon["squirtle"]["stats"], pokemon["squirtle"]["type"], [Moves("tackle")], None)
            else:
                return Pokemon("Pidgey", 5, pokemon["pidgey"]["stats"], pokemon["pidgey"]["type"], [Moves("tackle")], None)

if __name__ == "__main__":
    test_move()