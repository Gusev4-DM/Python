from random import choice


def get_jokes(num_iter):
    if num_iter > 5:
        return print('Введите не более 5')
    elif num_iter < 0:
        return print('Введите положительное число')
    random_words = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(num_iter):
        random_words.append(f'{(choice(nouns))} {(choice(adverbs))} {(choice(adjectives))}')
    print(random_words)


user_number = int(input('Введите количество шуток (не более 5-ти): '))
get_jokes(user_number)
