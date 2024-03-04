'''Модули и импорты'''

import sys
print(sys)
print(sys.builtin_module_names)
print(*sys.path, sep='\n')

######################################################################################################

# ● Антипримеры импорта

def randint(*args):
    return 'Не то, что вы искали!'

# Импортируем модуль random в основном файле проекта и попробуем сгенерировать случайное число от 1 до 6.

import random
print(random.randint(1, 6))
# Выдаст результат: "Не то что вы искали" потому что преимущественно ищет сначала из локальных файлов
# Хорошим тоном будет добавить в конце локального файла нижнее подчеркивание например "random_"

######################################################################################################

'''Использование from и as'''

from sys import builtin_module_names, path

print(builtin_module_names)
print(*path, sep='\n')

# Еще один вариант сочетания

import random as rnd
from sys import builtin_module_names as bmn, path as p
print(bmn)
print(*p, sep='\n')
print(rnd.randint(1, 6))
print(path) # NameError: name 'path' is not defined
print(sys.path) # NameError: name 'sys' is not defined


'''Плохой import * (импорт звёздочка)'''

# имеем файл super_module.py

from random import randint

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'

def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z

result = func(1, 6)

# Далее имеем файл main.py

from super_module import *

SIZE = 49.5

print(f'{SIZE = }\n{result = }')
print(f'{z = }') # NameError: name 'z' is not defined
print(f'{_secret = }') # NameError: name '_secret' is not defined
print(f'{func(100, 200) = }\n{randint(10, 20) = }')

def func(a: int, b: int) -> int:
    return a + b

print(f'{func(100, 200) = }')


'''
Переменная __all__ 
Список имен объектов, заключенных в кавычки т.е строки для импорта через "звездочку"
'''

# Все так же имеем файл super_module.py, только с новой переменной __all__

from random import randint

__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'

def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z

result = func(1, 6)


'''Виды модулей'''

# Попробуем добавить некоторую системность в модули. В Python есть:
# ● встроенные модули,
# ● установленные внешние модули,
# ● модули, созданные разработчиком, свои.

# Имеем файл base_math.py

"""Four basic mathematical operations.
Addition, subtraction, multiplication and division as functions.
"""
_START_SUM = 0
_START_MULT = 1
_BEGINNING = 0
_CONTINUATION = 1

def add(*args):
    res = _START_SUM
    for item in args:
    res += item
    return res

def sub(*args):
    es = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
    res -= item
    return res

def mul(*args):
    res = _START_MULT
    for item in args:
    res *= item
    return res

def div(*args):
    res = args[_BEGINNING]
    for item in args[_CONTINUATION:]:
    res /= item
    return res

if __name__ == '__main__':
    print(f'{add(2, 4) = }')
    print(f'{add(2, 4, 6, 8) = }')
    print(f'{sub(10, 2) = }')
    print(f'{mul(2, 2, 2, 2, 2) = }')
    print(f'{div(-100, 5, -2) = }')

# В новом файле пишем 

import base_math

x = base_math.mul # Плохой приём
y = base_math._START_MULT # Очень плохой приём
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)


'''Пишем свой модуль: __name__ == '__main__'
И добавляем в файл base_math.py конструкцию if __name == '__main__' '''


'''Создание пакетов и их импорт
Директория с __init__.py превразается в пакет'''


from mathematical import base_math as bm
from mathematical.advanced_math import exp

