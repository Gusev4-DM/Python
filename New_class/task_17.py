'''
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
'''

my_list = [1, 2, 1, 2, 3, 3, 4, 4]

# Решение 1

list_1 = []

for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
        list_1.append(i + 1)
print(f'Решение 1 {list_1}')

# Решение 2

list_2 = [i + 1 for i in range(len(my_list)) if my_list[i] % 2 != 0]
print(f'Решение 2 {list_2}')

# Решение 3

list_3 = [i + 1 for i, el in enumerate(my_list) if el % 2 != 0]
print(f'Решение 3 {list_3}')

