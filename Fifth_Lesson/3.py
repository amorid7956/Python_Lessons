with open("3.txt", "r") as f:
    count = 0
    amount = 0
    for line in f:
        salary =int(line.split()[1])
        if salary < 20000:
            print(line.split()[0], f'с окладом, меньше 20000({salary})')
        amount+=salary
        count+=1
    print('Средняя величина дохода сотрудников:', amount/count)