

'''Итераторы и генераторы'''


'''Однострочники'''

a = 42
b = 50
a, b = b, a
print(f'{a = }\t{b = }')


'''Распаковка'''

'''
Обычная
a, b, c = последовательность

Распаковка с упаковкой
a, *b, c = последовательность

Распаковка со звездочкой
*последовательность
'''


a, b, c = input("Три символа: ")
print(f'{a=} {b=} {c=}')

a, b, c = {"один", "два", "три", "четыре", "пять"}
print(f'{a=} {b=} {c=}') # ValueError: too many values to unpack (expected 3)

data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')


link ='https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')


# Распаковка со звездочкой

data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')


data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')
