from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, title='EmptyTitle'):
        self.title = title

    @abstractmethod
    def fabric_consumption(self):
        pass




class Coat(Clothes):  # Пальто
    def __init__(self, size=1):
        self.size = size

    def fabric_consumption(self):
        return (self.size / 6.5 + 0.5)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value > 0:
            self.__size = value
        else:
            print('Размер не может быть отрицательным!')


class Costume(Clothes):  # Костюм
    def __init__(self, height=1):
        self.height = height

    def fabric_consumption(self):
        return (self.height * 2 + 0.3)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            print('Рост не может быть отрицательным!')


costume = Costume(-33)  # декоратор @property раблотает
coat = Coat(-13)

costume.height = 42  # Присваиваем нормальные размеры
coat.size = 38

print(costume.fabric_consumption())
print(coat.fabric_consumption())

