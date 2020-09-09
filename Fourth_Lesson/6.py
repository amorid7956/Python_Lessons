from itertools import count, cycle

for el in count(3):
    if el == 10:  # Условие выхода из цикла
        break
    else:
        print(el, end=' ')
###################################
###################################
print('', end='\n')

words = ["first", "second", "third", "fourth"]
сount = 0
for el in cycle(words):
    if сount > 10:  # Условие при котором повторение элементов списка прекращается
        break
    print(el, end=' ')
    сount += 1
