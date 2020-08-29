integer = 2
str = 'Hello'
double = 3.14
dictionary = {'1': 'First', '2': 23}
list = [1, 2, 3, 4, 5, 6]
tup = (1, 2, 3)
print(integer, str, double, dictionary, list, tup, sep=' | ',end='\n')

i = int(input('Введите целое число: '))
s = input('Введите строку: ')
d = float(input('Введите десятичное число: '))
l = input('Введите список(через пробел): ').split(' ')
print(i, s ,d ,l, sep=' | ')