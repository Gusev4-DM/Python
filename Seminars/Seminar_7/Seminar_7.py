import math

sp = ["1", "2", "3", "4"]
sp1 = map(int, sp)
# for i in sp1:
    # print(i)


sp = [1, 2, 3, 4, 5]
sp1 = map(lambda x: x ** 2, sp)
# for i in sp1:
    # print(i)


sp = [1, 2, 3, 4, 5, 6]

sp = filter(lambda x: x % 2 == 0, sp)

# print(list(sp))


sp = [ x ** 2 for x in range(1, 6)]
sp = [ x for x in range(1, 6) if x % 2 == 0]

# sp = list(map(int, input('Введите число: ').split())) # Можно сделать инпут листа через пробле записывая числа
# sp = [int(i) for i in input('Введите число: ').split()] # - То же самое

sp = ['a', 'b', 'c']
numb = [1, 2, 3]
# print(list(zip(sp, numb)))
# print(*zip(sp, numb))

week = ['пн', 'вт', 'ср']
# for n, day in enumerate(week, 1):
#     print(n, '-', day)

'''
Задача 1. написать изначальную функцию transformation
'''

transformation = lambda x: x

values = [1, 23, 42, 'abcd']
transformed_value = list(map(transformation, values))

# if values == transformed_value:
#     print('Ok')
# else:
#     print('Fail')

'''
Задача 2.Найти площадь орбит, без равных друг другу элементов. по формуле S = pi * i[0] * i[1]
'''

def find_fathest_orbit(lst):
    sqare_orbits = [int(3.14 * val[0] * val[1]) for val in lst if val[0] != val[1]]
    max_index = sqare_orbits.index(max(sqare_orbits))
    return lst[max_index]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_fathest_orbit(orbits))

##############################################################################

def find_fathest_orbit(lst):
    sqare_orbits = [math.pi * i[0] * i[1] for i in lst if i[0] != i[1]]
    return lst[sqare_orbits.index(max(sqare_orbits))]
    

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_fathest_orbit(orbits))

##############################################################################

def find_fathest_orbit(lst):
    sqare_orbits = [i for i in lst if i[0] != i[1]]
    return max(sqare_orbits, key=lambda x: 3.14 * x[0] * x[1])  # Лямбду можно применять к ключам
    

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_fathest_orbit(orbits))

# Пример

sp = ['aweqda', 'adaw', 'z']
sp1 = max(sp, key=lambda x: len(x))
# print(sp1)

sp.sort(key=lambda x: len(x))

# Итерируемым объектам таким как max или sort можно задавать ключ куда можно закидывать лямбда функцию

'''
Задача 3. Написать функцию same_by которая проверяет все ли значения так же делятся без остатка
'''

def same_by(char, obj):
    for i in obj:
        if char(i) != char(obj[0]):
            return False
    return True


values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('defferent')
