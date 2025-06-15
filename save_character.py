import pandas as pd
from character import Character


class CharacterExporter():
    """
    Klasa odpowiedzialna za eksportowanie dancych postaci do pliku Excel.

    Zapisywana jest jedna postać do wskazanego arkusza pliku.
    """

    def __init__(self, file_path: str,  sheet_name: str):
        """
        Funckja inicjalizująca klasę CharacterExporter.

        Args:
            file_path (str): Ścieżka do pliku Excel, do którego mają być
            zapisane dane.
            sheet_name (str): Nazwa arkusza w pliku Excel.
        """
        self.file_path = file_path
        self.sheet_name = sheet_name

    def save_character(self, character: Character):
        """
        Funlkcja zbiera i zapisuje dane przekazanej postaci do pliku Excel.

        Args:
            character (Character): Obiekt postaci, której dane mają być
            zapisane.
        """

        data = {
            "Name": [character.name],
            "Class": [character.character_class],
            "Race": [character.character_race.random_race.name],
            "Strength": [character.stats["strength"]],
            "Dexterity": [character.stats["dexterity"]],
            "Constitution": [character.stats["constitution"]],
            "Intelligence": [character.stats["intelligence"]],
            "Wisdom": [character.stats["wisdom"]],
            "Charisma": [character.stats["charisma"]],
        }
        df1 = pd.DataFrame(data)

        with pd.ExcelWriter(self.file_path, mode='a', engine='openpyxl') as w:
            df1.to_excel(w, self.sheet_name, index=False)


if __name__ == "__main__":

    character_name = input("Enter character name: ")
    character_exporter = CharacterExporter("dnd.xlsx", "character")
    character_exporter.save_character(Character(character_name))
