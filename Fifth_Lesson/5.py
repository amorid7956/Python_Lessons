import random

with open("5.txt", "w") as f:
    s = ''
    for i in range(5):
        s += str(random.randint(1, 100)) + ' '
    f.write(s)

with open("5.txt", "r") as f:
    new_str = f.read().split()
    sum = 0
    for i in range(len(new_str)):
        sum += int(new_str[i])
    print('Сумма чисел в файле:', sum)
