# List comprehension

from os import system 
system("cls")

'''list = []            #  создаем список

for i in range(1, 101):
    # if(i%2 == 0):            # если остаток от деления равен 0
        list.append(i)

print(list) # [2, 4, 6, 8, 10, ...  86, 88, 90, 92, 94, 96, 98, 100] все четные числа до 100 '''

''' list = [i for i in range(1, 21)]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(list)

list = [i for i in range(1, 21) if i % 2 == 0]  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(list)

list = [(i, i) for i in range(1, 21) if i % 2 == 0]  # список кортежей [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12)...
print(list)'''

'''def f(x):
    return x**3

list = [(i, f(i)) for i in range(1, 11) if i % 2 == 0]  # число и его куб [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000)]
print(list)'''


