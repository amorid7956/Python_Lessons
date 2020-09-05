def my_func(*args):
    temp_list = []
    for i in range(len(args)):
        temp_list.append(args[i])
    sum = 0
    sum += max(temp_list) #Находим максимальный
    temp_list.remove(max(temp_list)) #Удаляем его из временного буфера
    sum += max(temp_list)   #И со вторым максимальным числом также
    temp_list.remove(max(temp_list))
    return sum


# Функция получилась универсальная -
# т.е принимает любое кол-во позиционных аргументов, и возвращает сумму 2-х самых больших
print(my_func(22, 41, 9))
print(my_func(22, 41, 9, 55, 64, 71, 5))
