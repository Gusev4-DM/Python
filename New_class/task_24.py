'''
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''


def some_func(my_list):
    flag = True
    while flag:
        flag = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                flag = True
    return my_list



my_list = [1, 6, 0, 9, 4, 5, 3, 15, 4, 10]
print(some_func(my_list))

