from random_race import RandomRace
from random_class import RandomClass
from import_race import RaceImporter
from import_class import ClassImporter
from manage_race_bonuses import ManageRaceBonuses


class Character():
    def __init__(self, name: str):
        self.name = name
        races = RaceImporter("dnd.xlsx", "race").races
        classes = ClassImporter("dnd.xlsx", "class").classes
        self.character_race = RandomRace(races)
        self.character_class = RandomClass(classes)
        self.stats = ManageRaceBonuses(
            self.character_race).calculate_final_statistics()

    def show_character(self) -> None:
        """Display character information"""
        print(f"\nCharacter Name: {self.name}")
        print(f"Race: {self.character_race.random_race.name}")
        print(f"Class: {self.character_class}")
        print("\nStatistics:")
        print(self.stats)


'''
if __name__ == "__main__":
    character_name = input("Enter character name: ")
    character = Character(character_name)
    character.show_character()
'''
