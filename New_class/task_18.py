'''
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
'''

my_str = 'Строки нумеруются начиная с единицы'.split()

max_l = len(max(my_str, key=len))

for i, el in enumerate(sorted(my_str), 1):
    print(f'{i}. {el:>{max_l}}')


text = "vsdsdsdsdsds dfsfdf fdfdfd fdfdfd".split()
shift = len(max(text))
for n, el in enumerate(sorted(text), 1):
    print(f"{n}. {el:>{shift}}")