'''
Задача 1 
Квадратное уравнение 5x^2-10x-400=0 последовательно сохраняя переменные a, b, c, d, x1 и x2
'''

from math import sqrt


a, b, c = 5, -10, 400
d = (b ** 2) - (4 * a * c)

if d < 0:
    print('Корней нет')
elif d > 0:
    x1 = (sqrt(d) - b) / (2 * a)
    x2 = (-sqrt(d) - b) / (2 * a)
    print(f'Корни {x1, x2}')
elif d == 0:
    print((-b) / (2 * a))

