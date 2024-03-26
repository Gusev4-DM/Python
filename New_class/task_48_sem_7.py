'''
✔ Доработаем предыдущую задачу 47.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
'''

from random import choices, randint
from string import ascii_lowercase


def func_1(ext, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files=1):
    for _ in range(files):
        name_file = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        with open(name_file, 'wb') as data:
            pass


def func_2(files=1, **kwargs):
    values = []
    for i in kwargs.values():
        values.append(i)
    for _ in range(files):
        ext = str(*choices(values))
        func_1(ext, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files=1)


func_2(5, a='.txt', b='.doc', c='.exe')