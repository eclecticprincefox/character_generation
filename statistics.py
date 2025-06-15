import random

# klasa stat i ta klasa ma jakąś metodę i pozostałe klasy Strenght itp dziedziczą po niej
# w klasie stat ma być metoda roll stat, w podklasach metoda jest nadpisywana i jest możliwość wywoływanioa  w trochę inny sap


class Stat:

    def __init__(self):
        self.value = self.roll_stat()

    def roll_stat(self) -> int:
        # Roll 4d6 and drop the lowest die
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.value}"
