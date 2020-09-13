with open("1.txt", 'w') as f:
    while True:
        s = input('Введите любую строку: ')
        if s:
           f.write(s +'\n')
        else:
            break

