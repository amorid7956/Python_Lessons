class Equipment_Warehouse:  # Склад оргтехники
    def __init__(self):
        self.equipment = {}

    @staticmethod
    def greetings(str):
        print(str)

    def acceptance_to_warehouse(self, *args):
        printers, scanners, xeroxes = args  # распаковка
        self.equipment[printers.title] = printers.number_printers
        self.equipment[scanners.title] = scanners.number_scanners
        self.equipment[xeroxes.title] = xeroxes.number_xeroxes
        print(self.equipment)

    def give_to_company(self, equip_numb_sub: int):
        for equip in self.equipment:
            self.equipment[equip] -= equip_numb_sub


class Office_Equipment:  # Оргтехника
    is_technics = True
    average_price = 12000


class Printers(Office_Equipment):
    __title = 'Printers'

    @property
    def title(self):
        return self.__title

    def __init__(self, number_printers):
        try:
            self.number_printers = number_printers
            if type(number_printers) == str:
                raise Exception
        except Exception as e:
            print('Введите количество числом')


class Scanners(Office_Equipment):
    __title = 'Scanners'

    @property
    def title(self):
        return self.__title

    def __init__(self, number_scanners):
        try:
            self.number_scanners = number_scanners
            if type(number_scanners) == str:
                raise Exception
        except Exception as e:
            print('Введите количество числом')

class Xeroxes(Office_Equipment):
    __title = 'Xeroxes'

    @property
    def title(self):
        return self.__title

    def __init__(self, number_xeroxes):
        try:
            self.number_xeroxes = number_xeroxes
            if type(number_xeroxes) == str:
                raise Exception
        except Exception as e:
            print('Введите количество числом')

# Инициализация объектов
warehouse = Equipment_Warehouse()
Equipment_Warehouse.greetings("Welcome to Equipment_Warehouse!")

printers = Printers('8')
printers = Printers(8)
print(printers.number_printers, printers.title, printers.is_technics, printers.average_price)
scanners = Scanners('QWERTY')
scanners = Scanners(12)
print(scanners.number_scanners, scanners.title)
xeroxes = Xeroxes('ERG3')
xeroxes = Xeroxes(9)
print(xeroxes.number_xeroxes, xeroxes.title)

warehouse.acceptance_to_warehouse(printers, scanners, xeroxes)  # {'Printers': 8, 'Scanners': 12, 'Xeroxes': 9}
warehouse.give_to_company(4)  # Отправляем по 4 штуки каждого оборудования в подразделение фирмы
print(warehouse.equipment)  # {'Printers': 4, 'Scanners': 8, 'Xeroxes': 5}
