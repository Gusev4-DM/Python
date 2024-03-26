'''
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
'''

# Решение 1

import random
import string


def gen_name(min_len, max_len):
    letters = [chr(i) for i in range(97, 123)]
    len_name = random.randint(min_len, max_len)
    name = []
    for _ in range(len_name):
        name.append(random.choice(letters))

    return ''.join(name).title()


def randome_text(len_text):
    return ''.join(random.choice(string.ascii_letters + string.digits, k=len_text))


def creat_file(type_file, qantity_files=1, min_len=6, max_len=30, min_byte=256, max_byte=4096):
    for _ in range(qantity_files):
        name_file = f'{gen_name(min_len, max_len)}.{type_file}'
        memory_file = random.choice([el for el in range(min_byte, max_byte + 1) if el % 8 == 0])
        with open(name_file, 'w', encoding='utf8-') as f:
            f.write(randome_text(memory_file))
            f.truncate(memory_file)


creat_file('txt')




