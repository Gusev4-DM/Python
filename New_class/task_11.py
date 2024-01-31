'''
Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
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
else:
    real = round(-b / (2 * a), 4)
    imag = round(sqrt(abs(d)) / (2 * a), 4)
    x1 = complex(real, imag)
    x2 = complex(real, -imag)
    print(f'x1 - {x1:.3f}, x2 - {x2:.3f}')
