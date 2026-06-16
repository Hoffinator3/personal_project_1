import sys
import json
import os
from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
#from pokemon.moves import Moves
from pokemon.battle import Battle
from trainers.player import Player
from trainers.trainer import Trainer


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

    #print(f"- Bulbasaur\nOriginal HP: {bulb_hp}\nDamage take: {s.moves[0].calculate_damage(s, b)}\nRemaining HP: {b.stats["hp"]}")

    # pokemon.usemove() test
    #print(f"use_move() test: {s.use_move('tackle')}")

def test_move():
    b = None
    s = None
    with open(os.path.abspath("./data/pokemon.json"), mode='r') as d:
        pokemon = json.load(d)
        b = Pokemon("Bulbasaur", 5, pokemon["bulbasaur"]["stats"], pokemon["bulbasaur"]["type"], [Moves("tackle")], None)
        s = Pokemon("Squirtle", 5, pokemon["squirtle"]["stats"], pokemon["squirtle"]["type"], [Moves("tackle")], None) 

    player = Player("zach", b)
    rival = Trainer("Red", s)
    fight = Battle(player, rival)
    

if __name__ == "__main__":
    test_battle()
    test_move()