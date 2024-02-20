'''
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
'''

def some_func(numbers, index_1, index_2):
    if index_1 >= index_2:
        print('Нет элементов')
    elif index_1 < 0 and index_2 > len(numbers):
        return sum(numbers)
    elif index_1 < 0:
        return sum(numbers[:index_2])
    elif index_2 > len(numbers):
        return sum(numbers[index_1 + 1:])
    else:
        return sum(numbers[index_1 + 1:index_2])
    

numbers = [10, 20, 30, 40, 50, 70, 80, 90, 15]
index_1 = 1
index_2 = 7
print(some_func(numbers, index_1, index_2))