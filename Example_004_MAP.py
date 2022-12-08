# Функция map

'''li = [x for x in range(1, 20)]
li = list(map(lambda x: x+10, li))    # list превращаем в список
print(li)   # 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]'''

'''data = list(map(int, input().split()))  # int - превращает лист из строк в лист чисел
print(data)  # [5, 8, 84, 1984, 36, 38] 

data = list(map(int, ' 8 98 108'. split()))

for e in data:
    print(e)

print('--')

for e in data:
    print(e) '''
  

def where(f, col):                       # описываем функцию, которая в качестве арг будет принимать функцию f и набор данных
    return [x for x in col if f(x)]      # возвращать будет некий список

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)     # map(int, data) - неполноценный список данных, на данном этапе map не будет преобразован в список
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
