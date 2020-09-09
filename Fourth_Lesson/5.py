from functools import reduce

#result_list = [i for i in range(100, 105) if i % 2 == 0] Лично проверил произведение 100*102*104 - ВЕРНО
result_list = [i for i in range(100, 1001) if i % 2 == 0]
composition = reduce(lambda a, b: a * b, result_list)
print('Произведение всех элементов списка: ', composition)
