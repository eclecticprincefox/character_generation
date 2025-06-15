class Race:
    def __init__(self, name, strength_bonus, dexterity_bonus, constitution_bonus,
                 intelligence_bonus, wisdom_bonus, charisma_bonus):
        self.name = name
        self.strength_bonus = strength_bonus
        self.dexterity_bonus = dexterity_bonus
        self.constitution_bonus = constitution_bonus
        self.intelligence_bonus = intelligence_bonus
        self.wisdom_bonus = wisdom_bonus
        self.charisma_bonus = charisma_bonus

    def __repr__(self):
        return (f"Race(name={self.name!r}, "
                f"strength_bonus={self.strength_bonus}, "
                f"dexterity_bonus={self.dexterity_bonus}, "
                f"constitution_bonus={self.constitution_bonus}, "
                f"intelligence_bonus={self.intelligence_bonus}, "
                f"wisdom_bonus={self.wisdom_bonus}, "
                f"charisma_bonus={self.charisma_bonus})")

    def __str__(self):
        return (f"{self.name}, "
                f"(STR: {self.strength_bonus}, "
                f"DEX: {self.dexterity_bonus}, "
                f"CON: {self.constitution_bonus}, "
                f"INT: {self.intelligence_bonus}, "
                f"WIS: {self.wisdom_bonus}, "
                f"CHA: {self.charisma_bonus})")
