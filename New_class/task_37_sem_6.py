'''
1. Создайте модуль с функцией внутри.
2. Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
3. Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
4. Функция выводит подсказки “больше” и “меньше”.
5. Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
'''

from random import randint

def guess_number(start, end, attempts):
    number = randint(start, end)
    while attempts > 0:
        my_number = int(input(f'Угадайте загаднное число от {start} до {end}, у вас {attempts} попыток. Ваш вариант: '))
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
    guess_number(1, 10, 5)

