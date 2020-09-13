result = {}
with open("6.txt", "r") as f:
    for line in f:#Первый цикл: извлекаем каждую строку из файла(Предмет и количества видов занятий)
        subj_list = line.split()
        lesson_hours = 0
        for i in range(1,len(subj_list)):#Второй цикл: от 1 до конца списка
            temp = ''
            for element in subj_list[i]:#Третий цикл: проверяем каждое число из списка sub_list,
                # чтобы потом привести к str к int
                if element.isdigit():
                    temp+=element
            if temp: #Прибавляем  строку, приведенную к int, для каждого вида занятий, если темп не пустая строка
                lesson_hours+=int(temp)
        result[subj_list[0][:-1]]=lesson_hours #{-1],Чтобы убрать двоеточие в конце названия предмета
print(result)