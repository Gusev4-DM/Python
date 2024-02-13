
'''
Функции
'''

a = 42
print(type(a), id(a))
print(type(id))

very_bad_programming_style = sum
print(very_bad_programming_style([1, 2, 3]))


'''
Опеределение собственной функции
Зарезервиванное слово def()
'''

def my_func():
    pass # ничего не делать

# Плохо:
if a != 5:
    pass
else:
    a += 1

# Уже лучше:
if a == 5:
    a += 1
else:
    pass

# Отлично. Ничего лишнего:
if a == 5:
    a += 1

'''
Аргументы функции
'''

def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | str: # Можем str поменять на None. Считается более универсальным методом
    # Это называется анотация типов
    '''
    Функция  принимает на вход 3 параметра: a, b, c целым и вещественным числом.
    На первый выход дает кортеж который содержит два ответа в вещественном виде tuple[float, float]
    На второй вывод так же возвращает вещественное число float
    На третию выход дает строку - "Нет рещения"
    '''
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений' # Или можем поменять на None. Считается более универсальным методом
    
print(quadratic_equations(2, -3, -9))


'''
Изменяемые и неизменяемые аргументы
'''

def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }') # Для демонстрации работы, но не для привычки принтить из функции
    return a

a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')

#########################################################################

def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
        print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
        return data
    
my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')

# Если мы передаем изменяемый объект то изменения произошедшие внутри функции так же затрагивают внешний объект

'''
Возврат значения return
● Если указан один объект — возвращается именно этот объект.
● Если указано несколько значений через запятую, возвращается кортеж с
перечисленными значениями
● Если ничего не указано после return — возвращается None
● Если return отсутсвует - Python "мысленно" дописывает в качестве последней строки функции return None
'''

def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None # Ее можно закоментировать. Пайтон сам ее допишет


'''
Неявный return
'''

def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
        print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
    # Здесь должна быть return data. Поэтому new_list имеет значение None

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')


'''
Значения по умолчанию
'''

def quadratic_equations(a, b=0, c=0): # Пробелы между знаком равенства не прнято ставить
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    
print(quadratic_equations(2, -9)) # -9 то значение b


'''
Изменяемый объект как значение по умолчанию. В качестве значения по умолчанию нельзя указывать изменяемы типы: списки,
словари и т.п. Это приведёт к неожиданным результатам:
'''

def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')

# Python будет использоваться список внутри функции каждый раз ее дополняя а не начиная все сначала, запоминая ее предыдущее значение.
# Плохой прием. Правильное решение будет снизу:

def from_one_to_n(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data

'''
Позиционные и ключевые параметры.
Косая черта / и звездочка * разделяют позиционные и ключевые параметры
'''

def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass

####################################################################################

def standard_arg(arg):
    print(arg)

standard_arg(42) # Позиционное значение. Оно попадает в первую позицию в перменную arg
standard_arg(arg=42) # Ключевой стиль. Мы указываем ключ arg и его значение 42

####################################################################################

def pos_only_arg(arg, /): # / Значит что переменная может получать значение только позционныым стилем
    print(arg)

pos_only_arg(42)
pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

####################################################################################

def kwd_only_arg(*, arg): # * Значит что переменная может получать значение только ключевым стилем
    print(arg)

kwd_only_arg(42) # TypeError: kwd_only_arg()
kwd_only_arg(arg=42)

####################################################################################

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    combined_example(1, 2, 3) # TypeError: combined_example() takes 2 positional arguments but 3 were given
    combined_example(1, 2, kwd_only=3)
    combined_example(1, standard=2, kwd_only=3)
    combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'


'''
Аргументы args и kwargs
'''

