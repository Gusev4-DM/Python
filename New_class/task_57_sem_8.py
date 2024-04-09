'''
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
'''

import csv
import pickle
from pathlib import Path

_PATH = Path.cwd() / 'task_6' / 'users.csv'


def csv_print(source_file: Path = _PATH) -> bytes:
    with open(source_file, 'r', newline='') as source:
        return pickle.dumps(list(csv.reader(source)))


print(csv_print())