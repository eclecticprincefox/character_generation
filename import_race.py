import pandas as pd
from race import Race


class RaceImporter:
    """
    Klasa impotrująca wszytskie rasy z pliku Excel.

    Zapisuje wszytskie rasy w rasces jako listę obiektów Race

    """

    def __init__(self, file_path: str, sheet_name: str):
        """
        Funckja inicjalizująca klasę RaceImporter.

        Args:
            file_path (str): Ścieżka do pliku Excel, do którego mają być
            zapisane dane.
            sheet_name (str): Nazwa arkusza w pliku Excel.
        """
        self.races = self.import_races(file_path, sheet_name)

    def import_races(self, file_path: str, sheet_name: str):
        """
        Funkcja importująca informację o rasach postaci z Excel.

        Args:
            file_path (str): Ścieżka do pliku Excel, do którego mają być
            zapisane dane.
            sheet_name (str): Nazwa arkusza w pliku Excel.

        Returns:
            List[Race]: Lista obiektów Race reprezentujących rasy postaci.
        """
        df = pd.read_excel(file_path, sheet_name)
        races = []
        for _, row in df.iterrows():
            races.append(
                Race(
                    name=row.iloc[0],
                    strength_bonus=row.iloc[1],
                    dexterity_bonus=row.iloc[2],
                    constitution_bonus=row.iloc[3],
                    intelligence_bonus=row.iloc[4],
                    wisdom_bonus=row.iloc[5],
                    charisma_bonus=row.iloc[6]
                )
            )
        return races


'''
importer = RaceImporter("dnd.xlsx",  "race")

# Wydrukuj wszystkie rasy
for race in importer.races:
    print(race)'''
