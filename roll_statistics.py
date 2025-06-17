import random


class Stats:
    """
    Klasa reprezentująca pojedynczą statystykę postaci 

    Przechowuje wartość statystyki oraz zawiera metode do
    losowania statystyki ((4k6, odrzuć najniższą kość))
    """

    def __init__(self) -> None:
        """
        Funkcja inicjalizuje obiekt Stat i losuje wartość statystyki.
        """
        self.value = self.roll_stat()

    def roll_stat(self) -> int:
        """
        Funkcja losuję wartość statystyki 4 randomowe liczby z
        zakresu od 1 do 6. Odrzucana jest jedna najmniejsza
        wylosowana wartość.

        Returns:
            int: Suma wylosowanych wartości jako statystykę
        """
        # Roll 4d6 and drop the lowest die
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)

    def __str__(self) -> str:
        """
        Funkcaj zwraca tekstową reprezentację statystyki.

        Returns:
            str: Nazwa i wartość statystyki w czytelnej formie.
        """

        return f"{self.__class__.__name__}: {self.value}"
