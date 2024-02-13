'''
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
'''

friends_stuff = {
    'Александр': ('палатка', 'топор', 'еда', 'пиво'),
    'Антон': ('палатка', 'вилка', 'вода', 'пиво'),
    'Влад': ('палатка', 'топор', 'вода', 'пиво'),
    'Дима': ('палатка', 'топор', 'вода', 'лимонад')
}

'''Код начинается с создания словаря friends_stuff,
который содержит в себе списки вещей, взятых друзьями во время похода.
Затем создается пустое множество set_1. В цикле происходит проверка
пересечений всех предметов, которые присутствуют у всех друзей,
и результат сохраняется в set_1.'''

set_1 = set()

for k in friends_stuff:
    if not set_1:
        set_1 = set(friends_stuff[k])
    else:
        set_1 &= set(friends_stuff[k])

print('Вещи взяли все три друга: ', set_1)

my_tuple = friends_stuff.keys()

my_set = set()

'''Далее в цикле for происходит перебор друзей,
затем для каждого друга находятся уникальные вещи,
которые принадлежат только ему, и выводятся в консоль.'''

for friends in my_tuple:
    my_set = set(friends_stuff[friends])
for other_friends in [i for i in my_tuple if i != friends]:
    my_set = my_set - set(friends_stuff[other_friends])
if my_set:
    print(f'Вещи уникальны, есть только у {friends}:', *my_set)

for friends in my_tuple:
    my_set = set()
    to_remove = set(friends_stuff[friends])
    for other_friends in [i for i in my_tuple if i != friends]:
        if not my_set:
            my_set = set(friends_stuff[other_friends])
        else:
            my_set = my_set & set(friends_stuff[other_friends])
    my_set -= to_remove
    if my_set:
        print(f'{friends} не взял \t {my_set}')

'''В последнем цикле также для каждого друга находятся вещи,
которые он не взял, но взяли другие, и эта информация
также выводится в консоль.'''

# Решение 2 от учителя

