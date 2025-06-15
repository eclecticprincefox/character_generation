import pandas as pd
import os
import random
from random_class import RandomRaceAndClass


class Character():
    def __init__(self, file_path: str, race_sheet: str, class_sheet: str):
        self.file_path = file_path

    def show_character(self):
        print(f"Character Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Race: {self.character_race}")
        print("Final Statistics:")
        for stat, value in self.final_character_statistics.items():
            print(f"{stat.capitalize()}: {value}")

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
    print("---------Character saved---------")
    character.save_character("dnd.xlsx")
