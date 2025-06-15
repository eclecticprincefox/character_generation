
class Class:
    """
    Klasa reprezentująca klasę postaci w grze.

    Przechowuje nazwę klasy postaci
    """

    def __init__(self, name: str):
        """
        Funkcja inicjalizuje obiekt Class z nazwą klasy.

        Args:
            name (str): Nazwa klasy.
        """
        self.name = name

    def __str__(self):
        """
        Funkcja zwraca tekstową reprezentację klasy

        Returns:
            str: Nazwa klasy
        """
        return (f"{self.name}")
