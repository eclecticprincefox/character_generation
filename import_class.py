from typing import List
import pandas as pd
from classs import Class


class ClassImporter:
    """
    Klasa impotrująca wszytskie klasy z pliku Excel.

    Zapisuje wszytskie klasy w classes jako listę obiektów Class
    """

    def __init__(self, file_path: str, sheet_name: str) -> None:
        """
        Funckja inicjalizująca klasę ClassImporter.

        Args:
            file_path (str): Ścieżka do pliku Excel, do którego mają być
            zapisane dane.
            sheet_name (str): Nazwa arkusza w pliku Excel.
        """
        self.classes = self.import_classes(file_path, sheet_name)

    def import_classes(self, file_path: str, sheet_name: str) -> List[Class]:
        """
        Funkcja importująca informację o klasach postaci z Excel.
        Args:
            file_path (str): Ścieżka do pliku Excel, do którego mają być
            zapisane dane.
            sheet_name (str): Nazwa arkusza w pliku Excel.

        Returns:
            List[Class]: Lista obiektów Class reprezentujących klasy postaci.
        """
        df = pd.read_excel(file_path, sheet_name)
        classes = []
        for _, row in df.iterrows():
            classes.append(
                Class(
                    name=row.iloc[0]
                )
            )
        return classes


'''
importer = ClassImporter("dnd.xlsx",  "class")

# Wydrukuj wszystkie rasy
for classs in importer.classes:
    print(classs)'''
