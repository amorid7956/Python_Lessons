class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    input_divider = int(input('Введите делитель для числа 100: '))
    if input_divider == 0:
        raise MyZeroDivisionError('Исключительная ситуация деления на 0')
except MyZeroDivisionError as e:
    print(e.txt)
except Exception:
    print('Неверный формат ввода')
else:
    result = 100 / input_divider
    print(f'Результат от деления 100 на {input_divider}:', result)
