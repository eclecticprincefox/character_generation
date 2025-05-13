import pandas as pd  
import random

class Character_Race:
    def _init_():
    
class Character_Class:
    def _init_():




class Character:
    def __init__(self, name: str, character_race: dict, character_class: dict):
        self.name = name
        self.race_data = character_race["Race"]
        self.class_data = character_class["Class"]
        self.stats = self.generate_stats()
        
     
       
    def generate_stats(self) -> dict:
        return {
            "Strength": self.roll_stat(),
            "Dexterity": self.roll_stat(),  
            "Constitution": self.roll_stat(),
            "Intelligence": self.roll_stat(),
            "Wisdom": self.roll_stat(),
            "Charisma": self.roll_stat()
        }
        
    def roll_stat(self) -> int:
        # Roll 4d6 and drop the lowest die
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)
    

class 

    df.pd.read_excel(data_path):
        # Load the data from the Excel file
        data_path = "data.xlsx"
        df = pd.read_excel(data_path, sheet_name=None)
        
    
class 

if __name__ == "__main__":
 
    data_path

your_character = input("Do you want to create a character? (yes/no): ")
if your_character == "yes":
    name = input("Enter your character's name: ")