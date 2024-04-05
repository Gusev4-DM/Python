''' СЕРИАЛИЗАЦИЯ '''


''' JSON '''

# Рассмотрим пример JSON файла

{
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": [ # Квардратные скобки а не фигурные 
        "Shanna@melissa.tv",
        "antonette@howel.com"
    ],
    "address": {
        "street": "Victor Plains",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "geo": {
            "lat": "-43.9509",
            "lng": "-34.4618"
        }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
        "name": "Deckow-Crist",
        "catchPhrase": "Proactive didactic contingency",
        "bs": "synergize scalable supply-chains"
    }
}

# ● Преобразование JSON в Python
# json_file = json.load(f) - Загрузка JSON из файла и сохранение в dict или list
# json_list = json.loads(json_text) - Загрузка JSON из строки и сохранение в dict или list

import json

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)

print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')


# Мы подготовили информацию в виде многострочного str в python и хотим превратить его из JSON строки в объекты Python

json_text = """
[
    {
        "userId": 1,
        "id": 9,
        "title": "nesciunt iure omnis dolorem tempora et
        accusantium",
        "body": "consectetur animi nesciunt iure dolore"
    },
    {
        "userId": 1,
        "id": 10,
        "title": "optio molestias id quia eum",
        "body": "quo et expedita modi cum officia vel magni"
    },
    {
        "userId": 2,
        "id": 11,
        "title": "et ea vero quia laudantium autem",
        "body": "delectus reiciendis molestiae occaecati non minima
        eveniet qui voluptatibus"
    },
    {
        "userId": 2,
        "id": 12,
        "title": "in quibusdam tempore odit est dolorem",
        "body": "praesentium quia et ea odit et ea voluptas et"
    }
]"""

print(f'{type(json_text) = }\n{json_text = }')
json_list = json.loads(json_text)
print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')



''' ● Преобразование Python в JSON '''


my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

print(f'{type(my_dict) = }\n{my_dict = }')
with open('new_user.json', 'w') as f:
    json.dump(my_dict, f)

# Как вы видите символы отличные от ASCII были заменены на специальные коды.

with open('new_user.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'{new_dict = }')

# Теперь все вновь работает


# Если же мы хотим отказаться от символов экранирования в JSON файле, следует установить дополнительный параметр ensure_ascii в значение ложь.
with open('new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)


# Воспользуемся словарём my_dict ещё раз для проверки функции dumps

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
    "путешествия"],
    "age": 35,
    "children": [
        {
        "first_name": "Алиса",
        "age": 5
        },
        {
        "first_name": "Маруся",
        "age": 3
        }
    ]
}

dict_to_json_text = json.dumps(my_dict)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')



''' ● Дополнительные параметры dump и dumps '''


res = json.dumps(my_dict, indent=2,
                 separator=(',',':'),
                 sort_keys=True)

# Параметр indent твечает за форматирование с отступами
# Параметр separator принимает на вход кортеж из двух строковых элементов
# 1. Первый - символ разделитель элементов
# 2. Второй - разделитель ключа и значение.
# Параметр sort_keys отвечает за сортировку ключей по алфавиту

my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}

res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=True)
print(res)



''' CSV '''


''' ● Чтение CSV '''

import csv

with open('biostats.csv', 'r', newline='') as f: # newline='' писать обязательно чтобы не было проблем с отступами
    csv_file = csv.reader(f) # Функция csv.reader принимает на вход файловый дескриптор и построчно читает информацию.
    for line in csv_file:
        print(line)
    print(type(line))


# Другой пример

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(line)
    print(type(line))

# ➢ dialect='excel-tab' — указали диалект с табуляцией в качестве разделителя
# ➢ quoting=csv.QUOTE_NONNUMERIC — передали встроенную константу, указывающую функции, что числа без кавычек необходимо преобразовать к типу float.


''' ● Запись CSV '''

# csv_write = csv.writer(f) - csv_write позволяет сохранять в формате CSV
# csv_write.writerow(line) - Сохранение списка в одной строке файла в формате CSV
# csv_write.writerows(all_data) - Сохранение матрицы в нескольких строках файла в формате CSV


with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
    else:
        line[2] += 1
        for j in range(2, 4 + 1):
            line[j] = int(line[j])
        all_data.append(line)
csv_write.writerows(all_data)


''' ● Чтение в словарь '''

# Воспользуемся классом DictReader.
# fieldnames - Список заголовков столбцов, ключей словаря
# restkey - Значение ключа для столбцов, которых нет в fieldnames
# restval - Значение поля ключей fieldnames, которых нет в файле CSV

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
    restkey="new", restval="MainOffice", dialect='excel-tab',
    quoting=csv.QUOTE_NONNUMERIC)

    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

# Другой вариант

with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office",
    dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)

    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')



''' ● Запись из словаря '''

# Параметрам класса DictWriter аналогичны параметрам DictReader
# csv_write.writeheader() - Сохранение первой троки с заголовками впорядке их перечисления в параметре fieldnames
# csv_write.writerow(line) - Сохранение списка в одной строке файла в формате CSV
# csv_write.writerows(all_data) - Сохранение матрицы в нескольких строках файла в фромет CSV

import csv
from typing import Iterator

with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read: Iterator[dict] = csv.DictReader(f_read, fieldnames=["name", "sex", "age", "height", "weight", "office"],
        restval="MainOffice", dialect='excel-tab',
        quoting=csv.QUOTE_NONNUMERIC)
    
    csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
        dialect='excel-tab', quoting=csv.QUOTE_ALL)
    
    csv_write.writeheader()
    all_data = []

    for i, dict_row in enumerate(csv_read):
        if i != 0:
            dict_row['id'] = i
            dict_row['age'] += 1
            all_data.append(dict_row)

    csv_write.writerows(all_data)



''' Модуль Pickle '''

'''
Python предлагает модуль pickle для сериализации и десериализации своих структур в поток байт. Преобразования возможны в любом месте и в любое время,
если вы используете Python. Но данные окажутся бесполезными, если вы передаёте их для обработки другим ЯП.
'''

import pickle
import os

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }')

os.system('echo Hello world!')


# Сериализация
# pickle.dump(my_dict, f) - Сохранение объекта в бинарном файле
# pickle.dumps(my_dict) - Сохранение объекта в строку байт

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
        "first_name": "Алиса",
        "age": 5
        },
        {
        "first_name": "Маруся",
        "age": 3
        }
    ]
}

print(my_dict)
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')
print(f'{pickle.DEFAULT_PROTOCOL = }')



def func(a, b, c):
    return a + b + c

my_dict = {
        "numbers": [42, 4.1415, 7+3j],
        "functions": (func, sum, max),
        "others": {True, False, 'Hello world!'},
}

with open('my_dict.pickle', 'wb') as f:
        pickle.dump(my_dict, f)


# Десериализация
# new_dict = pickle.load(f) - Загрузка из бинарноо файла и сохранение в объект
# new_dict = pickle.loads(data) - Получение объекта из бинарной строки

data = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'

new_dict = pickle.loads(data)
print(f'{new_dict = }')


def func(a, b, c):
    return a * b * c

with open('my_dict.pickle', 'rb') as f:
    new_dict = pickle.load(f)

print(f'{new_dict = }')
print(f'{new_dict["functions"][0](2, 3, 4) = }')
