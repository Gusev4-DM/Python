'''
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

import json
from pathlib import Path

# Решение 1

def txt_to_json(file_txt, file_json):
    with (open(file_txt, 'r', encoding='utf-8') as f_read,
          open(file_json, 'w', encoding='utf-8') as f_write
        ):
        data = {}
        for line in f_read:
            data[line.split()[0].capitalize()] = line.split()[1]
        json.dump(data, f_write, indent=4)

txt_to_json('text_result.txt', 'text_result.json')


# Решение 2

_PATH_SOURCE = Path.cwd() / 'task_1' / 'source'
_PATH_RESULT = Path.cwd() / 'task_1' / 'result.json'


def func(input_data: Path = _PATH_SOURCE, output: Path = _PATH_RESULT):
    with open(input_data, 'r', encoding='utf-8') as source, \
            open(output, 'w', encoding='utf-8') as result:
        data = {}
        while line := source.readline():
            data[line.split('|')[0].capitalize()] = float(line.split('|')[1].strip())
        json.dump(data, result, separators=(',\n', ':'))


if __name__ == '__main__':
    func()