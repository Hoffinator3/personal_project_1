from pokemon.pokemon import Pokemon


class Player:
    def __init__(self, name: str, team: list[Pokemon]):
        self.name = name
        self.team = team

    def list_moves(self):
        for mon in self.team:
            i = 1
            member = self.team[mon]
            for move in member.moves:
                print(f"{i}. {move.name}")
                i += 1
