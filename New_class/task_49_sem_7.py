'''
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

from os import getcwd, makedirs, chdir
from task_48_sem_7 import func_2

def func_3(some_dir):
    my_path = getcwd() + some_dir
    try:
        makedirs(my_path)
        chdir(my_path)
    except FileExistsError:
        chdir(my_path)
    func_2(5, a='.txt', b='.doc', c='.exe')
    chdir('..')


func_3('test_dir')