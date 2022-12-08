''' def f(x):
    return x**2

print(type(f))   # чем сама по себе является функция <class 'function'>
print(f(2))      # 4   '''

''' def calc1(x):
    return x+10

print(calc1(10))   # 20 '''

''' def calc2(x):
    return x*10

def math(op, x):
    print(op(x))

math(calc2, 10)  # 100 '''

'''def sum(x, y):       # функция сложения
    return x+y 

def mylt(x, y):      # функция умножения
    return x*y '''

# calc(mylt, 4, 5)      # указываем как аргумент функцию mylt и значения с которыми будет работать функция = 20

def calc(op, a, b):   # функция, которая в качестве аргумента принемает операцию, а в качестве операндов 2 аргумента
    print(op(a, b))
    
calc(lambda x, y: x+y, 4, 5)           # 9