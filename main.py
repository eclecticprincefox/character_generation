import pandas as pd
import os
import random


def roll_stat() -> int:
    # Roll 4d6 and drop the lowest die
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)


class Strength_stat:
    def __init__(self):
        self.stat = roll_stat()
        super().__init__()


class Dexterity_stat:
    def __init__(self):
        self.stat = roll_stat()
        super().__init__()


class Constitution_stat:
    def __init__(self):
        self.stat = roll_stat()
        super().__init__()


class Intelligence_stat:
    def __init__(self):
        self.stat = roll_stat()
        super().__init__()


class Wisdom_stat:
    def __init__(self):
        self.stat = roll_stat()
        super().__init__()


class Charisma_stat:
    def __init__(self):
        self.stat = roll_stat()
        super().__init__()


class Character_Stats(Strength_stat, Dexterity_stat, Constitution_stat, Intelligence_stat, Wisdom_stat, Charisma_stat):
    def __init__(self):
        Strength_stat.__init__(self)
        self.strength = self.stat
        Dexterity_stat.__init__(self)
        self.dexterity = self.stat
        Constitution_stat.__init__(self)
        self.constitution = self.stat
        Intelligence_stat.__init__(self)
        self.intelligence = self.stat
        Wisdom_stat.__init__(self)
        self.wisdom = self.stat
        Charisma_stat.__init__(self)
        self.charisma = self.stat


def read_excel_file(file_path: str, sheet_name: str) -> pd.DataFrame:

    df = pd.read_excel(file_path, sheet_name)
    return df


def random_element(file_path: str, sheet_name: str):
    df = pd.read_excel(file_path, sheet_name)
    if df.empty:
        return None
    random_row = df.sample(n=1).iloc[0]
    return random_row.to_dict()


class Character_Race:
    def __init__(self, file_path: str, sheet_name: str):
        race_data = random_element(file_path, sheet_name)
        if race_data is None:
            self.race_name = None
            self.strength_bonus = 0
            self.dexterity_bonus = 0
            self.constitution_bonus = 0
            self.intelligence_bonus = 0
            self.wisdom_bonus = 0
            self.charisma_bonus = 0

        else:
            self.race_name = list(race_data.values())[0]
            self.strength_bonus = list(race_data.values())[1]
            self.dexterity_bonus = list(race_data.values())[2]
            self.constitution_bonus = list(race_data.values())[3]
            self.intelligence_bonus = list(race_data.values())[4]
            self.wisdom_bonus = list(race_data.values())[5]
            self.charisma_bonus = list(race_data.values())[6]


class Character_Class:
    def __init__(self, file_path: str, sheet_name: str):
        class_data = random_element(file_path, sheet_name)
        if class_data is None:
            self.class_name = None
        else:
            self.class_name = list(class_data.values())[0]


class Character:
    def __init__(self, name: str, file_path: str, race_sheet: str, class_sheet: str):
        self.name = name
        self.race_data = Character_Race(file_path, race_sheet)
        class_data = Character_Class(file_path, class_sheet)
        self.character_race = self.race_data.race_name
        self.character_class = class_data.class_name
        self.stats = Character_Stats()
        self.final_character_statistics = {
            "strength": self.stats.strength + self.race_data.strength_bonus,
            "dexterity": self.stats.dexterity + self.race_data.dexterity_bonus,
            "constitution": self.stats.constitution + self.race_data.constitution_bonus,
            "intelligence": self.stats.intelligence + self.race_data.intelligence_bonus,
            "wisdom": self.stats.wisdom + self.race_data.wisdom_bonus,
            "charisma": self.stats.charisma + self.race_data.charisma_bonus,
        }

    def show_character(self):
        print(f"Character Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Race: {self.character_race}")
        print("Final Statistics:")
        for stat, value in self.final_character_statistics.items():
            print(f"{stat.capitalize()}: {value}")

    def show_race_bonus(self):
        print("-----------Character bonuses-----------")
        self.race_data.show_race()

    def save_character(self, file_path: str):
        data = {
            "Name": [self.name],
            "Class": [self.character_class],
            "Race": [self.character_race],
            "Strength": [self.final_character_statistics["strength"]],
            "Dexterity": [self.final_character_statistics["dexterity"]],
            "Constitution": [self.final_character_statistics["constitution"]],
            "Intelligence": [self.final_character_statistics["intelligence"]],
            "Wisdom": [self.final_character_statistics["wisdom"]],
            "Charisma": [self.final_character_statistics["charisma"]],
        }
        df1 = pd.DataFrame(data)
        if os.path.exists(file_path):
            try:
                existing = pd.read_excel(file_path, sheet_name='character')
                df1 = pd.concat([existing, df1], ignore_index=True)
            except Exception:
                pass

        with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
            df1.to_excel(writer, sheet_name='character', index=False)


if __name__ == "__main__":
    print("Welcome to the D&D Character Creator!")

build_character = input("Do you want to create a character? (Y/N): ")
if build_character == "Y":
    name = input("Enter your character's name: ")
    character = Character(name, "dnd.xlsx", "race", "class")
    print("---------Character Created---------")
    character.show_character()
    character.save_character("dnd.xlsx")
    print("---------Character saved---------")

    print("---------Double chceck stats---------")

    print("---------Character Stats---------")

    print(f"Strength: {character.stats.strength}")
    print(f"Dexterity: {character.stats.dexterity}")
    print(f"Constitution: {character.stats.constitution}")
    print(f"Intelligence: {character.stats.intelligence}")
    print(f"Wisdom: {character.stats.wisdom}")
    print(f"Charisma: {character.stats.charisma}")

    print("-----------Character bonuses-----------")

    character.show_race_bonus()
