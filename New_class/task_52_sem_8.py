'''
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
'''

import json
from pathlib import Path

# Решение 1

def load_user():
    try:
        with open('user_access.json', encoding='utf-8') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return {}


def sort_dict(my_dict):
    my_dict = sorted(my_dict.items())
    return {key: value for key, value in my_dict}


def user_dict():
    flag = True
    while flag:
        print('"стоп" - Для выхода')
        user_name = input('Введите ваше имя: ')
        if user_name == 'стоп':
            print('Программа завершена!')
            break
        list_id = open('text_id.txt', 'r', encoding='utf-8').read().split()
        print(f'Это списов идентификаторов {list_id}.')
        user_id = input('Введите ваш индентификатор: ')

        if user_id in list_id:
            print('Этот идентификатор уже существует!')
        else:
            access_level = int(input('Введите ваш уровень доступа: '))
            if 0 < access_level < 8:
                groups = load_user()
                groups[f'{access_level}'] = groups.setdefault(f'{access_level}', []) + [{user_id: user_name}]
                groups = sort_dict(groups)
                with open('user_access.json', 'w', encoding='utf-8') as file:
                    json.dump(groups, file, ensure_ascii=False)
                print(groups)
                with open('text_id.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{user_id} ')
            else:
                print('Введен некорректный код доступа')


user_dict()


# Решение 2

_PATH = Path.cwd() / 'task_2' / 'users.json'


def input_data():
    name = input('Enter name:\n')
    uid = input('Enter id:\n')
    access = input('Enter access level:\n')
    return access, uid, name


def get_id_list(path: Path):
    id_list = []
    with open(path, 'r', encoding='utf-8') as file:
        users = json.load(file)
        for entry in users.values():
            for uid in entry.keys():
                id_list.append(uid)
    return id_list


def save_user_data(path: Path = _PATH):
    id_list = get_id_list(path)
    while True:
        print("1. Enter user data.\n"
              "2. Quit.")
        choice = input()
        if choice == '2':
            quit()
        else:
            user = input_data()
            if user[1] in id_list:
                print('This user id already exists')
            else:
                id_list.append(user[1])
                with open(path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    data[user[0]][user[1]] = user[2]
                with open(path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, sort_keys=True)


if __name__ == '__main__':
    save_user_data()