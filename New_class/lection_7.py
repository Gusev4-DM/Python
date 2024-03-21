
''' Работа с файловой системой '''

f = open('text_data.txt', encoding='utf-8')
print(f)
print(list(f))

'''
● Режимы работы с файлами

Рассмотрим доступные режимы работы с файлами.
➢ 'r' — открыть для чтения (по умолчанию)
➢ 'w' — открыть для записи, предварительно очистив файл
➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже существует
➢ 'a' — открыть для записи в конец файла, если он существует
➢ 'b' — двоичный режим
➢ 't' — текстовый режим (по умолчанию)
➢ '+' — открыты для обновления (чтение и запись)

➢ 'r+' - не будет стирать файл
➢ 'w+' - сначала очистит файл, потом продолжит запись
'''



''' ● Метод close()
После завершения работы с файлом необходимо освободить ресурсы. Для этого
вызывается метод close().'''


f = open('text_data.txt', encoding='utf-8')
f.write('Окончание файла\n')
f.close

# ● Прочие необязательные параметры функции open

f = open('bin_data', 'wb', buffering=64) # wb - запись бинарных данных, с буфером в 64 байт информации
f.write(b'X' * 1200) # запишет 1200 иксов
f.close()

# Прочие необязательные апараметры функции open

'''
buffering - определяет режим буферизации
errors - используется только в текстовом режиме и определяет поведение в случае ошибок кодирования или декодирования
newline - отвечает запреобразование окончания строки
closefd - указывает оставлять ли файловый дескриптор открытым при закрытии файла
opener - позволяет передать пользовательскую функцию для открытия файла
'''


f = open('data.txt', 'wb') # при работе с бинарными данными кодировка не указывается
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

f = open('data.txt', 'r', encoding='utf-8')
print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decodebyte 0xec in position 14: invalid continuation byte
f.close()

f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()


# Менеджер контекста with open


with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Пока')) # ValueError: I/O operation on closedfile.

# with гарантирует закрытие файла и сохранение информации


# Старый прием открытия нескольких файлов
with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
        open('bin_data', 'rb') as f2, \
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))


# Новый способ открытия нескольких файлов
with (
    open('text_data.txt', 'r+', encoding='utf-8') as f1,
    open('bin_data', 'rb') as f2,
    open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
):
    print(list(f1))
    print(list(f2))
    print(list(f3))


# Чтение файла: целиком, через генератор

'''
list(f) - Чтение в список
res = f.read() - Чтение методом read
res = f.readline() - Чтение методом readline
for line in f: - Чтение циклом for
'''

# ● Чтение в список
with open('text_data.txt', 'r', encoding='utf-8') as f:
    print(list(f))



# ● Чтение методом read
with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')

# Другой вариант, прочитаем 100 символов
SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)



# ● Чтение методом readline. Для чтения текстового файла построчно используют метод readline
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)

# Передадим туда константу
SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)



# ● Чтение циклом for
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='') # Читаем от начала строки о символа переноса

# Передадим туда константу
SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1]) # Для переноса можно использовать срезы, используя строку от начального символа, кроме последнего где находится перенос строки
        print(line.replace('\n', '')) # Или так



''' Запись и добавление в файл '''


'''
res = f.write(text) - Запись методом write
f.writelines('\n'.joins(text)) - Запись методом writelines. Все записывает как одна строка, поэтому используем join и перенос строки
print(text, file=f) - print в файл
'''

'''
Режимы записи:

➢ w — создаём новый пустой файл для записи. Если файл существует, открываем его для записи и удаляем данные, которые в нём хранились.
➢ x — создаём новый пустой файл для записи. Если файл существует, вызываем ошибку.
➢ a — открываем существующий файл для записи в конец, добавления данных. Если файл не существует, создаём новый файл и записываем в него.
'''

# ● Запись методом write
text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text) # write возвращает количество байт\информации которое было записано
    print(f'{res = }\n{len(text) = }')


text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line) # Все будет в одну строку, потому что он не добавляет символ переноса строки
        # res = f.write(f'{line}\n') - Добавляем этот пернос строки таким образом
        print(f'{res = }\n{len(line) = }')


# ● Запись методом writelines
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text)) # Каждая строка будет записана с новой строки. Сама по себе не добавляет перенос


# ● print в файл
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f) # можно явно передать файловый объект для печати в файл. Доп.параметр file куда передаю перменную f. Добавляет переход на новую строку

# Другое решение
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f) # Добавит в конце строчки у звезды, перенесет строку и нарисует две решетки в тексте



''' Методы перемещения в файле '''


# ● Метод tell
# Метод tell возвращает текущую позицию в файле

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]

with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
print(f.tell()) # ValueError: I/O operation on closed file.


last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]


# ● Метод seek
# Метод seek позволяет изменить положение “курсора” в файле.
# seek(offset, whence=0), где offset — смещение относительно опорной точки, whence - способ выбора опороной точки.

with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))


# ● Метод truncate
# truncate(size=None) — метод изменяет размер файла
# Если не передать значение в параметр size будет удалена часть файла от текущей позиции до конца. Метод возвращает позицию после изменения файла.

last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())


size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))



''' Файловая система '''

# Работа с каталогами
# ● Текущий каталог

import os
from pathlib import Path

print(os.getcwd()) # Функция getcwd - выводит текущую директорию
print(Path.cwd()) # Вызываем класс Path. Так же выводит текущую директорию

# Для изменения текущего каталога можно воспользоваться функцией os.chdir. Она
# принимает на вход абсолютный или относительный путь до нового текущего каталога.

print(os.getcwd())
print(Path.cwd())
os.chdir('../..') # Перейти на ДВЕ папки выше
print(os.getcwd())
print(Path.cwd())


# ● Создание каталогов
os.mkdir('new_os_dir')
Path('new_path_dir').mkdir()

# Создание несколько вложенных друг в друга каталогов
os.makedirs('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True) # Дополнительный параметр parents=True указывает на необходимость создать всех недостающих родительских каталогов.


# ● Удаление каталогов
os.rmdir('dir') # OSError, папка не пустая
Path('some_dir').rmdir() # OSError, все так же, папка не пустая
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()

# Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и файлы), подойдёт функция из модуля shutil
import shutil

shutil.rmtree('dir/other_dir') # dir останется, other_dir удалиться со всем содержимым
shutil.rmtree('some_dir') # some_dir будет удален со всем содержимым


# ● Формирование пути
import os
from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')


''' Чтение данных о каталогах '''

# Для получения информации о том какие директории и файлы находятся в текущем каталоге можно воспользоваться следующими вариантами кода.
import os
from pathlib import Path

print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)


# ● Проверка на директорию, файл и ссылку
import os
from pathlib import Path

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')

p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')


# ● Обход папок через os.walk()
import os

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')


''' Работа с файлами '''
# Рассмотрим базовые операции по работе с файлами как с отдельными объектами.


# ● Переименование файлов
import os
from pathlib import Path

os.rename('old_name.py', 'new_name.py')

p = Path('old_file.py')
p.rename('new_file.py')

Path('new_file.py').rename('newest_file.py') # такое же как в строке 365 и 366


# ● Перемещение файлов
import os
from pathlib import Path

os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))
old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)


# ● Копирование файлов
# Для копирования файлов лучше всего подходит модуль shutil, который предоставляет ряд высокоуровневых операций.

import shutil
shutil.copy('one.txt', 'dir') # copy копирует информация из файла, но игнорирует метаданные
shutil.copy2('two.txt', 'dir') # copy2 попытается скопировать и метаданные


# Если стоит задача скопировать каталог со всем его содержимым в новое место, модуль предоставляет функции copytree
import shutil
shutil.copytree('dir', 'one_more_dir') # копирует информацию из каталога dir и называет ее one_more_dir


# ● Удаление файлов
import shutil
shutil.rmtree('dir')

# Если же необходимо удалить один файл, можно воспользоваться следующими вариантами:
import os
from pathlib import Path
os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()

