class Date:
    def __init__(self, date: str):
        self.date = '-'.join(date.split('.'))

    @classmethod
    def date_to_int(cls, str_date: str):
        try:
            result = int(''.join(str_date.split('-')))
        except ValueError:
            return 'Неверный формат даты'
        else:
            return result

    @staticmethod
    def date_validation(date: str):
        date_list = date.split('-')
        day = date_list[0]
        month =date_list[1]
        year= date_list[2]
        if int(day) < 1 or int(day) > 31 or int(month) < 1 or int(month) > 12 or 2000 < int(year) < 2020:
            return 'Дата не прошла валидацию'
        return 'Дата прошла валидацию'

input_date = input('Введите дату(дд.мм.гггг): ')
d = Date(input_date)
print('Значение даты в виде числа:', d.date_to_int(d.date))
print(d.date_validation(d.date))
