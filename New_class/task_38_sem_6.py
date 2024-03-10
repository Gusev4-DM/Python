'''
1. Улучшаем задачу 37.
2. Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
3. Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
4. Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
'''

from random import randint
from sys import argv


def guess_number_com(args):
    number = randint(args[0], args[1])
    attempts = args[2]
    while attempts > 0:
        my_number = int(input(f'Угадайте загаднное число от {args[0]} до {args[1]}, у вас {args[2]} попыток. Ваш вариант: '))
        if my_number < number:
            print(f'Заданное число больше')
        elif my_number > number:
            print(f'Заданное число меньше')
        else:
            print(f'Число угаданно. Число оставшихся попыток {attempts - 1}.')
            return True
        attempts -= 1
        print(f'Осталось попыток {attempts}')
    else:
        print(f'Попытки закончились. Загаданое число было - {number}.')
        return False


if __name__ == '__main__':
    args = [int(i) for i in argv[1:]]
    guess_number_com(args)