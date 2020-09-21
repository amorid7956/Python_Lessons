from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, title):
        self._title = title

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    def title(self):
        return self._title


class Coat(Clothes):  # Пальто
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):  # Костюм
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height

    def fabric_consumption(self):
        return self.height * 2 + 0.3


def total_consumtion(coat, costume):
    return f"Полный расход ткани равен: {coat.fabric_consumption() + costume.fabric_consumption()}"


costume = Costume('Костюм', 42)  # декоратор @property раблотает
coat = Coat('Пальто', 38)

print("Расход ткани на костюм равен:", costume.fabric_consumption())
print("Расход ткани на пальто равен:" , coat.fabric_consumption())

print(total_consumtion(coat,costume))
