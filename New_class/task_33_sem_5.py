'''
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
'''

# Решение 1 - Стандартное выражение

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# Решение 2 - Тернарный оператор

for i in range(1, 101):
    print('FizzBuzz') if i % 3 == 0 and i % 5 == 0 else print('Buzz') if i % 5 == 0 else print('Fizz') if i % 3 == 0 else print(i)


# Решение 3 - Генераторное выражение

generator = ('FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Buzz' if i % 5 == 0 else 'Fizz' if i % 3 == 0 else i for i in range(1, 101))
for i in generator:
    print(i)

