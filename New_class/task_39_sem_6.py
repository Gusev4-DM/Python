'''
1. Создайте модуль с функцией внутри.
2. Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
3. Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
'''


def some_func(qws, ans, count):
    i = 0
    tries = count
    while i <= count:
        u_ans = input(f'Введите ваш ответ: ').lower()
        if u_ans in ans:
            return f'Ответ верный! Количество попыток - {i + 1}.'
        elif u_ans not in ans:
            print(f'Ответ не верен! Осталось попыток - {tries}')
            tries -= 1
            i += 1
        else:
            if i == count:
                return 0


# print(some_func("Не лает, не кусает, в дом не пускает", ['замок', 'охранник', 'собака'], 3))

