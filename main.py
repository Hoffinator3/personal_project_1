import sys
import json
import os
from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
from pokemon.battle import Battle
from trainers.player import Player

path_pokemon_data = "./data/pokemon.json"

def create_starter(starter: str) -> list[Pokemon]:
    team = []
    with open(os.path.abspath(path_pokemon_data), mode='r') as d:
        pokemon = json.load(d)
        match starter.lower().strip():
            case "bulbasaur":
                team.append(Pokemon("Bulbasaur", 5, pokemon["bulbasaur"]["hp"], pokemon["bulbasaur"], pokemon["bulbasaur"]["type"], ["tackle"], None))
                return team
            case "charmander":
                team.append(Pokemon("Charmander", 5, pokemon["charmander"]["hp"], pokemon["charmander"], pokemon["charmander"]["type"], ["scratch"], None))
                return team
            case "squirtle":
                team.append(Pokemon("Squirtle", 5, pokemon["squirtle"]["hp"], pokemon["squirtle"], pokemon["squirtle"]["type"], ["tackle"], None))
                return team
            case _:
                return list("Error Creating Starter")


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <player_name>")
        sys.exit(1)

    player_name = sys.argv[1]

    print(f"""
        Hello, {player_name}! Welcome to the wonderful world of Pokemon!\n
        Which starter do you want?\n
        1: Bulbasaur, 2: Charmander, or 3: Squirtle?
    """)

    starter = input()
    print(f"starter input = {starter}")

    if starter == None or starter == "":
        raise Exception(f"invalid starter choice")
    else:
       team = create_starter(starter) 

    print(f"team = {team}")

    player = Player(player_name, team)
    pokemon = team[0]
    

    print(f""" 
        Player Name: {player.name}\n
        Player Team: {player.team}\n
        Pokemon Picked: {pokemon.name}\n
        Level: {pokemon.level}\n
        HP: {pokemon.hp}\n
        Stats: {pokemon.stats}\n
        Types: {pokemon.types}\n
        Moves: {pokemon.moves}
    """)




if __name__ == "__main__":
    main()
