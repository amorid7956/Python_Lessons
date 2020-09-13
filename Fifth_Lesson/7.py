import json

result_list = [] #КОНЕЧНОМ списке
first_dict = {}  #первый СЛОВАРЬ В КОНЕЧНОМ списке
second_dict = {} #второй СЛОВАРЬ В КОНЕЧНОМ списке
average_profit = 0 #средняя прибыль компаний
count = 0 #количество компаний с положительной прибылью(для расчета средней прибыли)
with open("7.txt", "r") as f, open("7_new.txt", "w") as new_f:
    for line in f:
        firm_info = line.split()#засчленяем строку на элементы
        firm_profit = int(firm_info[2]) - int(firm_info[3])#вычисляем прибыль каждой фирмы
        if (firm_profit > 0):
            average_profit += firm_profit
            count += 1
        first_dict[firm_info[0]] = firm_profit  #заполняем первый словарь {фирма : прибыль}
    average_profit //= count #вычисляем среднюю прибыль компаний
    second_dict['average_profit'] = average_profit
    result_list.append(first_dict)
    result_list.append(second_dict) #финальный список сформирован.
    print(result_list)

    json.dump(result_list,new_f) #сохраняем список в файл 7_new.txt в виде json объекта
