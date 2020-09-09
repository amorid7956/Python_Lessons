def fact(n: int):
    for el in range(1, n + 1):
        yield el


start = 1
for el in fact(9):
    start *= el
    print(f'{el}! =', start)
