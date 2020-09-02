L = [21, 34, 44, 65, 77, 51, 23, 44, 98] 
print(L)
if (len(L) % 2 == 1):
    Length = len(L) - 1
else:
    Length = len(L)
i = 0
while i < Length:
    temp = L.pop(i)
    L.insert(i + 1, temp)
    i += 2
print(L)
