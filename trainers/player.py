from pokemon.pokemon import Pokemon


class Player:
    def __init__(self, name: str, team: list[Pokemon]):
        self.name = name
        self.team = team

    def list_moves(self):
        member = self.team[0]
        for move in member.moves:
            print(f"{i}. {move.name}")
            i += 1
    
    def list_team(self):
        mons = []
        i = 1
        for mon in self.team:
            mons.append(f"\n{i}. {mon.name}")
            i += 1
        return mons
    
    def add_member(self, new_mon):
        if len(self.team) == 6:
            raise Exception("You can only have 6 pokemon at a time")
        self.team.append(new_mon)

    def switch_lead(self, new_lead_index):
        self.team[0], self.team[new_lead_index] = self.team[new_lead_index], self.team[0]

    def team_wipe(self):
        for mon in self.team:
            if mon.stats["hp"] > 0:
                return False
        return True