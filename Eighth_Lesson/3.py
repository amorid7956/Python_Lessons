class OnlyNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

"""
Введите число для занесения в список: 13
Введите число для занесения в список: 31
Введите число для занесения в список: 22
Введите число для занесения в список: 7
Введите число для занесения в список: qwe
Введён не числовой тип!
Введите число для занесения в список: rw
Введён не числовой тип!
Введите число для занесения в список: stop
[13, 31, 22, 7]
"""
number_list = []
while True:
    try:
        element = input('Введите число для занесения в список: ')
        if element.lower() == 'stop':
            break
        if not element.isdigit():
            raise OnlyNumberError('Введён не числовой тип!')
    except OnlyNumberError as e:
        print(e.txt)
        continue
    else:
        number_list.append(int(element))

print(number_list)