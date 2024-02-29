'''
✔ Продолжаем развивать задачу 30.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
'''

some_text = 'Это просто текст'

user_iter = iter({i: ord(i) for i in some_text}.items())

for i in range(5):
    print(next(user_iter))

print(f'new line\n{next(user_iter)}')
