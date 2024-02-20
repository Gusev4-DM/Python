'''
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''

def some_func(my_text):
    ch_list = []
    for i in my_text:
        ch_list.append(ord(i))
    return sorted(set(ch_list), reverse=True)


my_text = 'Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.'
print(some_func(my_text))


# Решение 2

def some_func(my_text):
    return sorted(set([ord(i) for i in my_text]), reverse=True)


my_text = 'Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.'
print(some_func(my_text))

