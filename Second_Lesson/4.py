words = input('Введите строку из нескольких слов, разделённых пробелами: ').split() #['first', 'second', 'third', 'veryverylongphrase']
for i in range(len(words)):
    if (len(words[i]) > 10):
        print(f'{i + 1}: {words[i][:10]}')  # выводим от 0 до 9 индексы
    else:
        print(f'{i + 1}: {words[i]}')
