whole_seconds = int(input('Введите количество секунд: '))
hours = whole_seconds // 3600
whole_seconds -= hours * 3600
minutes = whole_seconds // 60
whole_seconds -= minutes * 60
seconds = whole_seconds
if (hours < 10):
    hours = '0' + str(hours)
if (minutes < 10):
    minutes = '0' + str(minutes)
if (seconds < 10):
    seconds = '0' + str(seconds)
print(f'{hours}:{minutes}:{seconds}')
