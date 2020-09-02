my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
if (num >= max(my_list)):
    my_list.insert(0, num)
elif (num <= min(my_list)):
    my_list.insert(len(my_list), num)
else:
    cnt = my_list.count(num)
    pos = my_list.index(num) - 1
    my_list.insert(pos + cnt, num)
print(my_list)
