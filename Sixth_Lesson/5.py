class Stationery:
    title = 'Empty title'

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title=Stationery.title):
        super().__init__(title)

    def draw(self, attrPen=1):
        super().draw()
        print(f"Метод для ручки: {attrPen}\n")


class Pencil(Stationery):

    def __init__(self, title=Stationery.title):
        super().__init__(title)

    def draw(self, attrPencil=2):
        super().draw()
        print(f"Метод для карандаша: {attrPencil}\n")


class Handle(Stationery):

    def __init__(self, title=Stationery.title):
        super().__init__(title)


# Инициализация объектов
NewPen = Pen('Ручка')
NewPencil = Pencil('Карандаш')
NewPHandle = Handle()  # без параметров выведет 'Empty title'

#Применение методов
NewPen.draw(33)
NewPencil.draw()
NewPHandle.draw()
