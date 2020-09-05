def Division_Of_Two_Numbers(divisible, divider):
    try:
        result = divisible / divider
    except ZeroDivisionError:
        print("На 0 нельзя делить.")
    else:
        print("Частное от деления: ", result)


numbers = input('Введите делимое и делитель, разделённые пробелом: ').split()
try:
    Division_Of_Two_Numbers(int(numbers[0]), int(numbers[1]))
except IndexError:
    print("Введите нужное количество аргументов.")
