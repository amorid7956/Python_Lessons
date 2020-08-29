import math
proceeds = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))
differ = proceeds - costs
if differ > 0:
    print('Ваша компания процветает')
    profitability = differ / proceeds
    print('Ретабельность компании: ', profitability)
    staff = int(input('Сколько сотрудников в вашей компании? '))
    average_profitability = profitability / staff
    print('Прибыль фирмы в расчете на одного сотрудника составляет: ',  round(average_profitability,3))
elif differ < 0:
    print('Ваша компания разорятся')
else:
    print('Ваша компания стоит на месте')
