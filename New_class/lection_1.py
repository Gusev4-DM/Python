color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зеленый':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика')
    case _:
        print('Тебя не понять')

# Интересная конструкция, работает от Python 3.10 +

year = int(input('Введите год в формате уууу: '))
if year % 4 != 0:
    print('Год обычный')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный')
    else:
        print('Обычный')
else:
    ('Високосный')

# Или запишем это условие вот так

if year % 4 != 0 or year % 100 == 0 and year % 400 == 0:
    print('Обычный')
else:
    print('Вискосный')

# Ленивый if

"""
if year % 4 != 0 or year % 100 == 0 and year % 400 == 0:

Если первый блок if покажет истину то дальше мы не будем проверять
"""

# Проверка на вхождение (in)

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введите число: '))
if num not in data:
    print('Число не внутри')

if num in data:
    print('Число не внутри')

# Тернарный оператор (if-else)

my_math = int(input('2 + 2 = '))
if 2 + 2 == my_math:
    print('Верно')
else:
    print('Вы уверены?')

my_math = int(input('2 + 2 = '))
print('Верно' if 2 + 2 == my_math else 'Вы уверены?')


'''
Циклы
'''

num = int(input('Введите число: '))
count = 0
while count < num:
    print(count)
    count += 2

########################################################################

num = float(input('Введите число: '))
STEP = 2
limit = num - STEP
count = -STEP
while count < limit:
    count += STEP
    if count % 12 == 0:
        continue
    print(count)

########################################################################

min_limit = 0
max_limit = 10

while True:
    print('Введите число между', min_limit, 'и', max_limit, '?')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
print('Было введено число', num)

########################################################################

min_limit = 0
max_limit = 10
count = 3
num = None

while count > 0:
    print(f'Количество попыток {count}')
    count -= 1

    num = float(input(f'Введите число между {min_limit} и {max_limit}: '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break

else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()

print('Все верно. Было введено число', num)

########################################################################

'''
Цикл for in
'''

########################################################################

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for i in data:
    print(i)


num = int(input('Введите число: '))
for i in range(0, num, 12):
    print(i)


animals = ['cat', 'dog', 'wolf', 'rate', 'dragon']
for i, item in enumerate(animals, start=1):
    print(i, item)

