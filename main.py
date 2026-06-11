import sys
from pokemon.pokemon import Pokemon
from pokemon.moves import Moves
from pokemon.battle import Battle
from trainers.player import Player

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <player_name>")
        sys.exit(1)

    print(f"Hello, {sys.argv[1]}! Welcome to the wonderful world of Pokemon!")

if __name__ == "__main__":
    main()
