'''
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
'''

import json
import csv
from pathlib import Path

# Решение 1

def convert_files():
    classes_access = []
    users = []
    with open('user_access.json', encoding='utf-8') as file:
        data = json.load(file)
    for key, value in data.items():
        classes_access.append(key)
        users.append(value)
    print(classes_access, users, sep='\n')

    with open('user_access.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        for i in range(len(classes_access)):
            writer.writerow(''.join(classes_access[i].split()))
            writer.writerow(users[i])


convert_files()

# Решение 2


_PATH_1 = Path.cwd() / 'task_2' / 'users.json'
_PATH_2 = Path.cwd() / 'tasks_3_4' / 'users.csv'


def json_to_csv(source_path: Path = _PATH_1, output_path: Path = _PATH_2):
    with open(source_path, 'r', encoding='utf-8') as source, \
            open(output_path, 'w', encoding='utf-8', newline='') as output:
        data = json.load(source)
        data_list = []
        for access, person in data.items():
            for uid, name in person.items():
                data_list.append([uid, name, access])
        writer = csv.writer(output)
        writer.writerow(['uid', 'name', 'access'])
        writer.writerows(data_list)


if __name__ == '__main__':
    json_to_csv()

