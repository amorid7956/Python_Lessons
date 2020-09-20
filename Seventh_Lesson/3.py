class Cell:
    def __init__(self, cell_numbers=1):
        self.cell_numbers = cell_numbers

    def __str__(self):
        return f'У данной клетки {self.cell_numbers} ячеек'

    def __add__(self, other):
        return Cell(self.cell_numbers + other.cell_numbers)

    def __sub__(self, other):
        return Cell(self.cell_numbers - other.cell_numbers) if self.cell_numbers > other.cell_numbers else \
            'Результирующее количество ячеек не может быть меньше 0'

    def __mul__(self, other):
        return Cell(self.cell_numbers * other.cell_numbers)

    def __truediv__(self, other):
        return Cell(self.cell_numbers // other.cell_numbers)

    def make_order(self, cell_number=1):
        s = ''
        temp = self.cell_numbers
        while temp >= cell_number:
            s += (cell_number * '*') + '\n'
            temp -= cell_number
            if temp < cell_number:
                s += (temp * '*')
                break
        print(s)


a = Cell(12)
b = Cell(4)
c = a + b
print(c, '\n')

c = a - b
print(c, '\n')

c = b - a
print(c, '\n')

c = a * b
print(c, '\n')

c = a / b
print(c, '\n')

a.make_order(5)
