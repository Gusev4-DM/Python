'''
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''

import random

def gen_name():
    letters = [chr(i) for i in range(97, 123)]
    vowel_letters = ('e', 'u', 'o', 'a', 'i', 'y')
    len_name = random.randint(4, 7)
    flag = True

    while flag:
        names = []
        for _ in range(len_name):
            names.append(random.choice(letters))
        if any(letter in vowel_letters for letter in names): # Проверяет есть ли хоть 1 гласная буква в слове
            flag = False
    
    print(''.join(names).title())
    return ''.join(names).title()


def write_names(name_file, count):
    for _ in range(count):
        with open(name_file, 'a', encoding='utf-8') as f:
            f.write(f'{gen_name()}\n')


write_names('text_names.txt', 7)