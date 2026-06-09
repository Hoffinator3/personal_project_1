from type_enum import Type

class Pokemon:
    def __init__(self, name: str, type_one: Type, type_two: Type | None, hp: int, phy_attack: int, phy_defense: int, spec_attack: int, spec_defense: int, speed: int, ability: str, weight: float) -> None:
        self.name = name
        self.type_one = type_one
        if type_two:
            self.type_two = type_two
        else:
            self.type_two = None
        self.hp = hp
        self.phy_attack = phy_attack
        self.phy_defense = phy_defense
        self.spec_attack = spec_attack
        self.spec_defense = spec_defense
        self.speed = speed
        self.ability = ability
        self.weight = weight
