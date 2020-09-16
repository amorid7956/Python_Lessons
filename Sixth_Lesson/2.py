class Road:
    _width = 0
    _length = 0

    def __init__(self, width=1, length=1):
        self._width = width #защищённые атрибуты
        self._length = length

    def weight_calc(self, weigth_nominal=1, deep=1):
        return (self._length * self._width * weigth_nominal * deep)/1000


r = Road(20, 5000)
print(f'Масса всего полотна: {r.weight_calc(25,5)} т')

