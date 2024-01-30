'''
Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
'''

import decimal
from math import pi

def area(d):
    decimal.getcontext().prec = 42
    return decimal.Decimal(pi * (d / 2) ** 2)

d = int(input('Введите диаметр: '))

print(area(d))