import random
from statistics import Stat


class Strength(Stat):
    def roll_stat(self) -> int:
        # Można np. rzucać inną kością, jeśli chcesz zmienić sposób losowania
        rolls = [random.randint(1, 6) for _ in range(5)]
        rolls.remove(min(rolls))
        return sum(rolls)


class Dexterity(Stat):
    def roll_stat(self) -> int:
        # zwykłe nadpisywanie bez zmienaimia
        return super().roll_stat()

# nizej przykłąd dla braku napisywania - po prostu dziedziczenie


class Constitution(Stat):
    pass


class Intelligence(Stat):
    pass


class Wisdom(Stat):
    pass


class Charisma(Stat):
    pass


if __name__ == "__main__":
    stats = [
        Strength(),
        Dexterity(),
        Constitution(),
        Intelligence(),
        Wisdom(),
        Charisma()
    ]

    for stat in stats:
        print(stat)
