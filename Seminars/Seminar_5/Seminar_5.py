import random

# def fact(x):
#     res = 1
#     for i in range(1, x + 1):
#         res *= i
#     return(res)

# print(fact(5))


''' Факториал 5!  ->   1 * 2 * 3 * 4 * 5 '''
# res = 1
# for i in range(1, 6):
#     res *= i
# print(res)

'''
5! = 5 * 4!  Факсториал 5 это факториал 4 умноженое на 5 итд
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1
'''


''' РЕКУРСИЯ'''

# def fact_r(x):
#     if x == 0:
#         return 1
#     return x * fact_r(x - 1)
    
# print(fact_r(5))

#######################################################################################

''' Задача 1.
Последовательность фибоначи в рекурсии
'''

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []

# for i in range(1, 11):
#     list_1.append(fib(i))

# print(list_1)

''' Задача 2.
Заменить максимальное на минимальное значение в списке. input 5 -> 1 2 3 4 5. output -> 1 2 3 4 1
'''

numbers = list(random.randint(1, 10) for _ in range(10))
print(numbers)
numbers[numbers.index(max(numbers))], numbers[numbers.index(min(numbers))] = numbers[numbers.index(min(numbers))], numbers[numbers.index(max(numbers))]
print(numbers)

numb = [int(x) for x in input().split()]
print(numb)
max_n = max(numb)
for i in range(len(numb)):
    if numb[i] == max_n:
        numb[i] = min(numb)

print(*numb)

lst = [int(i) for i in '1 3 3 3 4'.split()]
mx, mn = max(lst), min(lst)
lst_str = [str(i) for i in lst]
print(' '.join(lst_str).relace(str(mx), str(mn)))

'''Задача 3.
Написать программу которая принимает одно число и проверяет, является ли оно простым
'''


# def func(numbers):
#     for i in range(2, numbers // 2 + 1):
#         if numbers % i == 0:
#             return 'No'
#     return 'Yes'


# print(func(int(input('Введите число: '))))


# def is_prime(a):
#     if a < 2:
#         return False
#     for i in range(2, int(a ** 0.5 + 1)):
#         if a % i == 0:
#             return False
#     else:
#         return True
    

# print(is_prime(int(input())))

''' Задача 4.
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Нельзя использовать массивы и циклы. input 2 -> 3 4. output -> 4 3.
'''

# def reverse(num):
#     if len(num) == 0:
#         return []
#     return [num[-1]] + reverse(num[:-1])

# num = [1, 2, 3, 4]


# print(reverse(num))


# def in_out(n):
#     if n == 0:
#         return
#     k = input('Введите число: ')
#     in_out(n - 1)
#     print(k, end=' ')

# n = int(input('Введите число n: '))
# in_out(n)


def nums_mirror(n):
    temp = input('Введите число N: ')
    if n == 1:
        return temp
    print(temp, end=" ")
    return nums_mirror(n - 1) + temp

print(nums_mirror(5))