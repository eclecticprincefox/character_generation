import random
from statistics import Stat


class Strength(Stat):
    """
    Klasa reprezentująca statystykę Siły postaci.

    Dziedziczy po Stat i nadpisuje metodę roll_stat, aby losować w
    inny sposób niż bazowo.
    """

    def roll_stat(self) -> int:
        """
        Funkcaj losuje wartość siły rzucając 5k6 i odrzucając najniższy wynik.
        Dodane w celu pokazania możliwości modyfikacji.

        Returns:
            int: Wylosowana wartość siły.
        """
        rolls = [random.randint(1, 6) for _ in range(5)]
        rolls.remove(min(rolls))
        return sum(rolls)


class Dexterity(Stat):
    """
    Klasa reprezentująca statystykę zręcznoąci postaci.

    Dziedziczy po Stat i nadpisuje metodę roll_stat
    """

    def roll_stat(self) -> int:
        """
        Funkcja losuje wartość zręczności nadpisując domyślne roll_stat,
        ale nic w nim nie modyfikuje.

        Returns:
            int: Wylosowana wartość zręczności.
        """
        return super().roll_stat()

# nizej przykłąd dla braku napisywania - po prostu dziedziczenie


class Constitution(Stat):
    """
    Klasa reprezentująca statystykę sprawości postaci.

    Dziedziczy po Stat i nie nadpisuje nic.
    """
    pass


class Intelligence(Stat):
    """
    Klasa reprezentująca statystykę inteligencji postaci.

    Dziedziczy po Stat i nie nadpisuje nic.
    """
    pass


class Wisdom(Stat):
    """
    Klasa reprezentująca statystykę mądrości postaci.

    Dziedziczy po Stat i nie nadpisuje nic.
    """
    pass


class Charisma(Stat):
    """
    Klasa reprezentująca statystykę charyzmy postaci.

    Dziedziczy po Stat i nie nadpisuje nic.
    """
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
