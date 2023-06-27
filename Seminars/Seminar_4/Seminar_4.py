import random

'''
Задача 1. создать кортеж и записать в него 10 случайных чисел.
'''

numbers = tuple(random.randint(1, 10) for _ in range(10))

print(numbers)
print(numbers[0])

numbers = list(numbers) - #перевод кортежа в список

numbers[0] = 15 - # изменить кортеж невозможно, число в 0-м индексе не заменится

'''
Задача 2. Создать кортеж, заполненеый случайными числами. Написать метод, который заменяет элемент в кореже по заданому индексу случайным числом.
'''

def change_element(numbers, index):
     return numbers[:index] + (random.randint(1, 100), ) + numbers[index + 1:]

numbers = tuple(random.randint(1, 10) for _ in range(10))
index = 4

print(numbers)
numbers = change_element(numbers, index)
print(numbers)

'''
Задача 3. На вход подаются два числа. Напишите метод, который вернет сумму, разность, произведение и частное этих чисел
'''

def get_some_numbers(num_1, num_2):
    summa = num_1 + num_2
    multi = num_1 * num_2
    division = num_1 / num_2
    return print(f'Сумма - {summa}, Умножение - {multi}, Деление - {division}.')

num_1 = 5
num_2 = 2

get_some_numbers(num_1, num_2)

##############################################################################

def calculate(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2


def zadacha_1():
    num_f = 9
    num_s = 3
    
    summ, deduct, multi, division = calculate(num_f, num_s)
    print(summ, deduct, multi, division)

zadacha_1()
 
##############################################################################

def method(a, b):
    return a + b, a - b, a * b, a / b

result = method(5, 2)
summ = result[0]
deduct = result[1]
multi = result[2]
division = result[3]

print(summ, deduct, multi, division)


'''
Задача 4. Сгенерируйте список случайных чисел от 1 до 20 состоящий из 10 элементов.
Удалите из списка дубликаты уже имеющихся элементов. Опеределите, сколько элементов было удалено
'''

def get_uniq_numbers():
    numbers = [random.randint(1, 10) for _ in range(10)]
    deleted_num = len(numbers) - len(set(numbers))
    print(f'Количество удаленных элементов - {deleted_num}.')

get_uniq_numbers()

'''
Актереов разделили на списки по трем качествам, умные, красивые, сильные. На главную роль нужен атер обладающий всеми тремя каечствами.
Определите, сколько есть претендентов на главную роль
'''

beautiful = {"Илья", "Федор", "Семен", "Олег", "Лев", "Антон", "Артем", "Боря", "Стас", "Марк", "Ян"}
smart = {"Илья", "Георгий", "Лев", "Демьян", "Антон", "Владислав", "Боря", "Стас", "Марк", "Влад"}
strong = {"Федор", "Георгий", "Олег", "Демьян", "Артем", "Елисей", "Боря", "Стас", "Влад"}

candidates = beautiful.intersection(smart, strong) # .intersection() Позволяет найти  пересечения между итерируемыми объектами set
print(candidates)

###############################################################################

beautiful = set("Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян".split())
smart = set("Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад".split())
strong = set("Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад".split())

top = beautiful & smart & strong # - & работает с множествами, в отличии от AND который работает с логическими операндами
print(top)

