import sys
import json
import os
from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
from pokemon.battle import Battle
from trainers.player import Player
from trainers.trainer import Trainer
from battle.battle_loop import battle_loop

path_pokemon_data = "./data/pokemon.json"

def create_starter(starter: str) -> list[Pokemon]:
    team = []
    with open(os.path.abspath(path_pokemon_data), mode='r') as d:
        pokemon = json.load(d)
        match starter.lower().strip():
            case "bulbasaur" | "1":
                team.append(Pokemon("Bulbasaur", 5, pokemon["bulbasaur"]["stats"], pokemon["bulbasaur"]["type"], [Moves("tackle")], None))
                team.append(Pokemon("Pidgey", 5, pokemon["pidgey"]["stats"], pokemon["pidgey"]["type"], [Moves("tackle")], None))
                return team
            case "charmander" | "2":
                team.append(Pokemon("Charmander", 5, pokemon["charmander"]["stats"], pokemon["charmander"]["type"], [Moves("scratch")], None))
                team.append(Pokemon("Pidgey", 5, pokemon["pidgey"]["stats"], pokemon["pidgey"]["type"], [Moves("tackle")], None))
                return team
            case "squirtle" | "3":
                team.append(Pokemon("Squirtle", 5, pokemon["squirtle"]["stats"], pokemon["squirtle"]["type"], [Moves("tackle")], None))
                team.append(Pokemon("Pidgey", 5, pokemon["pidgey"]["stats"], pokemon["pidgey"]["type"], [Moves("tackle")], None))
                return team
            case _:
                return list("Error Creating Starter")

def create_rival(starter: str) -> list[Pokemon]:
    rival = []
    with open(os.path.abspath(path_pokemon_data), mode='r') as d:
        pokemon = json.load(d)
        match starter.lower().strip():
            case "squirtle" | "3":
                rival.append(Pokemon("Bulbasaur", 5, pokemon["bulbasaur"]["stats"], pokemon["bulbasaur"]["type"], [Moves("tackle")], None))
                #rival.append(Pokemon("Pidgey", 5, pokemon["pidgey"]["stats"], pokemon["pidgey"]["type"], [Moves("tackle")], None))
                return rival
            case "bulbasaur" | "1":
                rival.append(Pokemon("Charmander", 5, pokemon["charmander"]["stats"], pokemon["charmander"]["type"], [Moves("scratch")], None))
                #rival.append(Pokemon("Pidgey", 5, pokemon["pidgey"]["stats"], pokemon["pidgey"]["type"], [Moves("tackle")], None))
                return rival
            case "charmander" | "2":
                rival.append(Pokemon("Squirtle", 5, pokemon["squirtle"]["stats"], pokemon["squirtle"]["type"], [Moves("tackle")], None))
                #rival.append(Pokemon("Pidgey", 5, pokemon["pidgey"]["stats"], pokemon["pidgey"]["type"], [Moves("tackle")], None))
                return rival
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

    valid_starters = {
        "1": "bulbasaur",
        "2": "charmander",
        "3": "squirtle",
        "bulbasaur": "bulbasaur",
        "charmander": "charmander",
        "squirtle": "squirtle",
    }
    while True:
        starter = input("> ").strip().lower()

        if starter in valid_starters:
            starter = valid_starters[starter]
            break

        print("Invalid choice. Please try again.")

    team = create_starter(starter) 
    rival_team = create_rival(starter)

    player = Player(player_name, team)
    rival = Trainer("Red", rival_team)

    winner = battle_loop(player, rival)
    print(f"\n\n *** Battle Ended **\n\nYOU {winner}")


if __name__ == "__main__":
    main()
