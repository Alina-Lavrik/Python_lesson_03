# Задача. В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# [(2,4), (8, 64), (38, 1444)]

'''path ='file.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []   #  создаем пустой список, который в дальнейшем будем наполнять

while data != '':   # пока строка не пустая
    space_pos = data.index(' ') # найти первую позицию пробела
    numbers.append(int(data[:space_pos])) 
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)'''

def select(f, col):                      # принимает функцию f и какой-то набор данных col
    return [f(x) for x in col]           # формируем новый список и сразу его возвращаем

def where(f, col):                       # описываем функцию, которая в качестве арг будет принимать функцию f и набор данных
    return [x for x in col if f(x)]      # возвращать будет некий список

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res)
print(res)
