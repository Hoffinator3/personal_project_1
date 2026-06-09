from type_enum import Type

class Pokemon:
    def __init__(self, weight: float, type_one: Type, type_two: Type, ability: str):
        self.weight = weight
        self.type_one = type_one
        self.type_two = None
        self.ability = ability