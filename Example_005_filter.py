# Функция ﬁlter 

'''data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data))  # list - преобразуем к списку
print(res)                # [0, 2, 4, 6, 8]'''

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)     # map(int, data) - неполноценный список данных, на данном этапе map не будет преобразован в список
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)   # [(2, 4), (8, 64), (38, 1444)]

