sum = 0
special_sym = 'Q'
is_special = True
while is_special:
    user_in = input('Введите числа, разделённые пробелами, '
                    'или же введите специальный символ \"Q\"для выхода из программы: ').split()
    for num in user_in:
        if num.isdigit():
            sum += int(num)
        elif num == special_sym:
            print('Выход из программы')
            is_special = False
            break

    print('Сумма введённых чисел: ',sum)