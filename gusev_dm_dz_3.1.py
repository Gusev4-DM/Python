numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': ' три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

def translate_numbers(user_numbers, numbers):
    return numbers[user_numbers] if user_numbers in numbers.keys() else None

user_numbers = input('пропишите число от 0 до 10 на английском языке :')
print(translate_numbers(user_numbers, numbers))