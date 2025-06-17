from random_race import RandomRace
from import_race import RaceImporter
from create_statistics import Strength, Dexterity, Constitution, \
    Intelligence, Wisdom, Charisma


class ManageRaceBonuses():
    """
    Klasa odpowiedzialna za zarządzanie bonusami rasowymi postaci.

    Przechowuje informacje o bonusach wynikających z wybranej rasy
    i umożliwia obliczenie końcowych statystyk postaci.
    """

    def __init__(self, character_race: str = "random") -> None:
        """
        Funkcja odpowiedzialna za dodawanie bonusów rasowych postaci do
        wylosowanych statystyk.

        Oblicza końcowe statystyk postaci.
        """
        races = RaceImporter("dnd.xlsx", "race").races
        self.race = RandomRace(races)
        self.character_race = character_race

        self.stats = [
            Strength(),
            Dexterity(),
            Constitution(),
            Intelligence(),
            Wisdom(),
            Charisma()
        ]
        self.race_bonuses = [
            self.race.random_race.strength_bonus,
            self.race.random_race.dexterity_bonus,
            self.race.random_race.constitution_bonus,
            self.race.random_race.intelligence_bonus,
            self.race.random_race.wisdom_bonus,
            self.race.random_race.charisma_bonus
        ]

    def calculate_final_statistics(self) -> dict:
        """
        Funkcja odpowiedzialna za dodawanie bonusów rasowych postaci do
        wylosowanych statystyk.

        Oblicza końcowe statystyk postaci, zwraca słownik z wartościami
        statystyk z uwzględnieniem bonusów rasowych.
        """

        return {
            "strength": self.stats[0].value + self.race_bonuses[0],
            "dexterity": self.stats[1].value + self.race_bonuses[1],
            "constitution": self.stats[2].value + self.race_bonuses[2],
            "intelligence": self.stats[3].value + self.race_bonuses[3],
            "wisdom": self.stats[4].value + self.race_bonuses[4],
            "charisma": self.stats[5].value + self.race_bonuses[5]
        }


if __name__ == "__main__":
    manager = ManageRaceBonuses()
    final_stats = manager.calculate_final_statistics()
    print("Random race:", manager.race.random_race)
    print("Final stats with racial bonuses:")
    for stat, value in final_stats.items():
        print(f"{stat.capitalize()}: {value}")
