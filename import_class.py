import pandas as pd
from classs import Class


class ClassImporter:
    def __init__(self, file_path: str, sheet_name: str):
        self.classes = self.import_classes(file_path, sheet_name)

    def import_classes(self, file_path: str, sheet_name: str) -> pd.DataFrame:
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
