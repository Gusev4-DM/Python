'''

from modul1 import max_1   1. Альтернативный вариант импорта, импортируя только саму функцию max_1

from modul1 import *       2. * - обозначает импортировать все из этого модуля

import modul1              3. Импортировать модуль полностью, притаком виде импорта надо прописывать нажвание модуля и его функции. Например: print(modul1.max_1(5, 10))

import modul1 as m1        4. Можно заменить название на любое другое и вместо полного названия модуля использовать его. Например: print(m1.max_1(5, 10))

'''

# def sum_numbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
#     print('стоп')


# a  = sum_numbers(5, 'qwerty')
# print(a)


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i

#     return(res)

# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r', 'f'))
# print(sum_str(1, 8, 9)) # ошибка

''' Импорт модуля и обращение к нему, сначала обращаемся к модулю, затем к его функции указывая аргументы '''

# print(max_1(10, 9))

''' Рекурсия это функция вызывающая сама себя '''

def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []

for i in range(1, 10):
    list_1.append(fib(i))

print(list_1)

'''
АЛГОРИТМЫ это набор инструкция для выьпоенния некотрых задач. Любой фрагмент программного кода можно назвать алгоритмом.
Расмотрим 2 самых интеерсных алгоритма сортировок:
 - Быстрая соритровка
 - Соритровка слиянием
'''

# Быстрая сортировка

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 5, 2]))

# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1,72,36,7,7,5,4,13,5,96,8,29,4,12]

merge_sort(list_1)
print(list_1)
            

