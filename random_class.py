import random
from import_class import ClassImporter


class RandomClass:
    """
    Klasa odpowiedzialna za losowy wybór klasy postaci z dostępnej listy klas.

    Przechowuje wylosowaną klasę postaci.
    """

    def __init__(self, classes: list) -> None:
        """
        Inicjalizuje obiekt RandomClass i losuje klasę postaci 
        z listy dostępnych klas.

        Args:
            classes (list): Lista dostępnych klas postaci.
        """
        self.random_class = random.choice(classes)

    def __str__(self) -> str:
        """
        Zwraca nazwę wylosowanej klasy postaci jako tekst.

        Returns:
            str: Nazwa klasy postaci.
        """
        return (f"{self.random_class}")


if __name__ == "__main__":

    class_importer = ClassImporter("dnd.xlsx", "class")
    availible_classes = class_importer.import_classes("dnd.xlsx", "class")
    generator = RandomClass(availible_classes)
    print(generator)
