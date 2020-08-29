number_str = input('Введите целое положительное число: ')
max = int(number_str[0])
for i in number_str[1:]:
    if (int(i) > max):
       max = int(i)
    else:
        continue
print(max)