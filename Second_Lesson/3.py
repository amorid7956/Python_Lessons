month = int(input('Введите номер месяца от 1  до 12: '))
Seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
for season, month_numb in Seasons.items():
    if month in month_numb:
        print(f'Время года - {season}')
        break
