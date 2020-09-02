L = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

Keys = []
result = {}
for i in range(len(L)):
    for key in L[i][1].keys():
        if (key not in Keys):
            Keys.append(key)
            # 2 цикла, в целях проверки, если бы у нас в каждом кортеже было бы разнае количество ключей
for i in range(len(Keys)):
    result[Keys[i]] = []
    # В качестве значений результирующего словаря, задаём пустыми списками, чтобы применить .append()
for i in range(len(L)):
    for key, value in L[i][1].items():
        if value not in result[key]:
            result[key].append(value)
print(result)
