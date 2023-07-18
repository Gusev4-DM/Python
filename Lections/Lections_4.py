def f(x):
    return x*x

a = f

# print(a(5))

# print(type(a))

def calc_2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))
'''
calc_1 = lambda a,b: a + b
'''

# math(lambda a, b: a + b, 5, 45)

# Вывести только четные числа и возвести их в квадрат

'''
data = [1, 2, 3, 5, 8, 15, 23, 38]

res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i ** 2))

print(res)
'''

# ///////////////////////////////////////////////// Функция lambda /////////////////////////////////////////////////////////////////////


def select(f, col):              # selecet - тоже самое что и функция map
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = select(int, data)
# print(res)
res = where(lambda x: x % 2 == 0, res)
# print(res)
res = list(select(lambda x: (x, x ** 2), res))
# print(res)

'''
Если в алгоритмах выше заменить функцию select функцией map то ничего не поменяется. Решение будет такое же

Функция Where так же работает как и функция filter, если их заменить то ничего не меняется
'''

# //////////////////////////////////////////////// Функция map //////////////////////////////////////////////////////////////////////

list_1 = [x for x in range(1, 20)]
# print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

data = '15 156 96 3 5 8 52 5'

data = list(map(int, data.split()))
# print(data)


# ///////////////////////////////////////////////// Функция filter /////////////////////////////////////////////////////////////////////

data = [15, 65, 9, 36, 175]

res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# ///////////////////////////////////////////////// Функция zip /////////////////////////////////////////////////////////////////////

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
# print(data)

# ///////////////////////////////////////////////// Функция enumerate /////////////////////////////////////////////////////////////////////

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)

# ///////////////////////////////////////////////// Работа с файлами /////////////////////////////////////////////////////////////////////

'''
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w') # Здесь указываем режии в котором будем работать.
data.writelines(colors) # Разделителей не будет
data.close()
'''

'''
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

'''

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()


# ///////////////////////////////////////////////// Модуль OS /////////////////////////////////////////////////////////////////////

'''
import os
os.chdir() - Смена текущей директории
print(os.getcwd()) - Текущая рабочая директория
print(os.path.basename('D:/Python/Lections/Lections_4.py')) - Базовое имя пути. # Lections_4.py
print(os.path.abspath('Lections_4.py')) - Нормализованный абсолютный путь # D:/Python/Lections/Lections_4.py

'''

# ///////////////////////////////////////////////// Модуль shutil /////////////////////////////////////////////////////////////////////

'''
import shutil
shutil.copyfule(src, dst) - Копирует содердимое( но не метаданные) файла src в файл dst.
shutil.copy(src, dst) - Копирует содержимое файлы src в файл или папку dst.
shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории. path должен указывать неа директорию, а не на символическую ссылку
'''

