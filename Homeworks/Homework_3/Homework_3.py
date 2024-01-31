# Домашнаяя Задача 1. 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

numbers = int(input('Введите количество элементов списка А: '))
mass = []

for i in range(numbers):
    number = int(input('Введите сами числа: '))
    mass.append(number)

X = int(input('Введите число X, которое необходимо найти в списке: '))
count = 0
for i in range(numbers):
    if mass[i] == X:
        count += 1
print(f'Число {X} встречается в списке A {count} раз') 

# Домашняя Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

numbers = int(input('Введите количество элементов списка А: '))
mass = []

for i in range(numbers):
    mass.append(int(input(f'Введите сами число массива номер {i + 1}: ')))

X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))

result = mass[0]
min_distance = abs(X - mass[0]) # 2 - 4 = 2 асболютное, мин = 2
for i in range(1, numbers):
    distance = abs(X - mass[i]) # 2 - 4 = 2
    if min_distance > distance: # если 2 - 4 > 2
        result = mass[i]        # запиши его в резалт

print(f'В массиве {mass} самый близкий по величине элемент к числу {X} это {result}')


# Домашняя Задача 3.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

en_ru = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
'D': 2, 'G': 2,
'B': 3, 'C': 3, 'M': 3, 'P': 3,
'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
'K': 5,
'J': 8, 'X': 8,
'Q':10, 'Z': 10,
'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
'Й': 4, 'Ы': 4,
'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
'Ш': 8, 'Э': 8, 'Ю': 8,
'Ф': 10, 'Щ': 10, 'Ъ': 10}

word = input('Введите слово: ')

result = 0
for letter in word.upper():
    result += en_ru.get(letter, 0)

print(f'Стоимость слова "{word}": {result}')