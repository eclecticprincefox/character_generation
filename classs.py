
class Class:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return (f"Race(name={self.name!r}")

    def __str__(self):
        return (f"{self.name}")
