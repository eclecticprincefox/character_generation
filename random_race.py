import random
from import_race import RaceImporter


class RandomRace:
    """
    Klasa odpowiedzialna za losowy wybór rasy postaci z dostępnej listy ras.

    Przechowuje wylosowaną rasę postaci wraz z jej atrybutami statystyk.
    """

    def __init__(self, races: list) -> None:
        """
        Inicjalizuje obiekt RandomRace i losuje rase postaci (w tym jej nazwe
        i bonusy statystyk) z listy dostępnych ras.

        Args:
            races (list): Lista dostępnych ras postaci.
        """
        self.random_race = random.choice(races)

    def __str__(self) -> str:
        """
        Zwraca nazwę i bonusy wylosowanej klasy postaci jako tekst.

        Returns:
            str: Informacja o rasie postaci.
        """
        return (f"{self.random_race}")


if __name__ == "__main__":

    race_importer = RaceImporter("dnd.xlsx", "race")
    availible_races = race_importer.import_races("dnd.xlsx", "race")
    generator = RandomRace(availible_races)
    print(generator)
