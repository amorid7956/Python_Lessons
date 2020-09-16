class Worker:
    name = 'EmptyName'
    surname = 'EmptySurName'
    position = 'Emptyposition'
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name=Worker.name, surname=Worker.surname, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Оклад сотрудника: {self._income["wage"]}, Премия сотрудника: {self._income["bonus"]}')


obj_1 = Position()  # Проверяем пустой объект, без аргументов
obj_1.get_full_name()
obj_1.get_total_income()

obj_1 = Position('Ivan', 'Petrov', 50000, 8600)  # Проверяем объект с реальными данными
obj_1.get_full_name()
obj_1.get_total_income()
