class Race:
    """
    Klasa reprezentująca rasę postaci w grze.

    Przechowuje nazwę rasy oraz bonusy do wszystkich głównych statystyk
    postaci.
    """

    def __init__(self, name: int, strength_bonus: int, dexterity_bonus: int,
                 constitution_bonus: int, intelligence_bonus: int,
                 wisdom_bonus: int, charisma_bonus: int) -> None:
        """
        Funkcja inicjalizuje obiekt Race z nazwą rasy oraz bonusami do
        statystyk.

        Args:
            name (str): Nazwa rasy.
            strength_bonus (int): Bonus do siły.
            dexterity_bonus (int): Bonus do zręczności.
            constitution_bonus (int): Bonus do sprawności.
            intelligence_bonus (int): Bonus do inteligencji.
            wisdom_bonus (int): Bonus do mądrości.
            charisma_bonus (int): Bonus do charyzmy.

        """
        self.name = name
        self.strength_bonus = strength_bonus
        self.dexterity_bonus = dexterity_bonus
        self.constitution_bonus = constitution_bonus
        self.intelligence_bonus = intelligence_bonus
        self.wisdom_bonus = wisdom_bonus
        self.charisma_bonus = charisma_bonus

    def __str__(self) -> str:
        """
        Funkcja zwraca tekstową reprezentację rasy wraz z jej bonusami
        do statystyk.

        Returns:
            str: Nazwa rasy i jej bonusy do statystyk w czytelnej formie.
        """
        return (f"{self.name}, "
                f"(STR: {self.strength_bonus}, "
                f"DEX: {self.dexterity_bonus}, "
                f"CON: {self.constitution_bonus}, "
                f"INT: {self.intelligence_bonus}, "
                f"WIS: {self.wisdom_bonus}, "
                f"CHA: {self.charisma_bonus})")
