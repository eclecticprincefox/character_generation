import random
from import_race import RaceImporter


class RandomRace:
    def __init__(self, races):
        self.random_race = random.choice(races)

    def __repr__(self):
        return (f"Race(name={self.random_race!r})")

    def __str__(self):
        return (f"{self.random_race}")


if __name__ == "__main__":

    race_importer = RaceImporter("dnd.xlsx", "race")
    races = race_importer.import_races("dnd.xlsx", "race")
    generator = RandomRace(races)

    # Wyświetlenie
    print(generator)
