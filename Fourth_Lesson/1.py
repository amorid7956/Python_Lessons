import sys


def calc_salary(production: int, rate: int, prize: float):
    total = production * rate + prize
    print('Заработная плата сотрудника составляет: ', total)


try:
    calc_salary(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
except IndexError:
    print('Неверное количество аргументов.')
