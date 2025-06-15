import random
from import_class import ClassImporter


class RandomClass:
    def __init__(self, classes):
        self.random_class = random.choice(classes)

    def __repr__(self):
        return (f"Class(name={self.random_class!r})")

    def __str__(self):
        return (f"{self.random_class}")


if __name__ == "__main__":

    class_importer = ClassImporter("dnd.xlsx", "class")

    classes = class_importer.import_classes("dnd.xlsx", "class")

    generator = RandomClass(classes)

    # Wyświetlenie
    print(generator)
