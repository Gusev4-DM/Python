
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
Аргументы *args и **kwargs
Имена args и kwargs - общепринятое соглашение

def func(*args) - Принимает любое число позиционных аргументов
def func(**kwargs) - Принимает любое число ключевых аргументов
def func(*args, **kwargs) - Принимает любое число и позиционных и ключевых аргументов
'''

# Аргумент *args

def mean(args):
    return sum(args) / len(args)

print(mean([1, 2, 3]))
print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given

# Другой пример

def mean(*args): # *args - превращает внутри значение в кортеж, и уже затем работает с ним
    return sum(args) / len(args)

print(mean(*[1, 2, 3])) # ошибок не будет. * означает следующее: Распакуй список, каждое значение списка передай как отдельный элемент в функцию
print(mean(1, 2, 3))

# Аргумент **kwargs

def school_print(**kwargs): # *kwargs превращается в словарь, и уже потом работает с ним
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')

school_print(химия=5, физика=4, математика=5, физра=5)


'''
Области видимости: global и nonlocal
● локальная — код внутри самой функции, т.е. переменные заданные в теле
функции.
● глобальная — код модуля, т.е. переменные заданные в файле py содержащем
функцию.
● не локальная — код внешней функции, исключающий доступ к глобальным
переменным.
'''


# Локальные переменные:

def func(y: int) -> int:
    x = 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1

x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')


# ● Глобальные переменные:

def func(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }') # Для демонстрации работы, но не ля привычки принтить из функции
    return y + 1

x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')


# ● Не локальные переменные:

def main(a):
    x = 1
    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
        return y + 1
    return x + func(a)

x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')


# Доступ к константам

LIMIT = 1_000

def func(x, y):
    result = x ** y % LIMIT
    return result

print(func(42, 73))


# Анонимная функция lambda

def add_two_def(a, b):
    return a + b

add_two_lambda = lambda a, b: a + b # Это запись через лямбду. Не совсем 

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

# Правильное использование lambda

my_dict = {'two': 2, 'six': 6, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')


'''
Функции “из коробки”. Они же - встроенные функции которые достуны всегда, без импортов и других подготовительных операций.

abs(), aiter(), all(), any(), anext(), ascii(), bin(), bool(), breakpoint(), bytearray(), bytes(),
callable(), chr(), classmethod(), compile(), complex(), delattr(), dict(), dir(), divmod(),
enumerate(), eval(), exec(), filter(), float(), format(), frozenset(), getattr(), globals(),
hasattr(), hash(), help(), hex(), id(), input(), int(), isinstance(), issubclass(), iter(), len(),
list(), locals(), map(), max(), memoryview(), min(), next(), object(), oct(), open(), ord(),
pow(), print(), property(), range(), repr(), reversed(), round(), set(), setattr(), slice(),
sorted(), staticmethod(), str(), sum(), super(), tuple(), type(), vars(), zip().
'''


'''
Изучим map(), filter(), zip()
'''


# map(function, iterable) — принимает на вход функцию и последовательность.
# Функция применяется к каждому элементу последовательности и возвращает map итератор.

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)


# filter(function, iterable) — принимает на вход функцию и последовательность.
# Если функция возвращает истину, элемент остаётся в последовательности. Как и map возвращает объект итератор.

numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)


# zip(*iterables, strict=False) — принимает несколько последовательностей и итерируется по ним параллельно.
# Если передать ключевой аргумент strict=True, вызовет ошибку ValueError в случае разного числа элементов в каждой из последовательностей.

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]

for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')


'''
Изучим max(), min(), sum()
'''

# max(iterable, *[, key, default]) или max(arg1, arg2, *args[, key])
# Функция принимает на вход итерируемую последовательность или несколько позиционных элементов и ищет максимальное из них.
# Ключевой параметр key указывает на то, какие элементы необходимо сравнить, если объект является сложной структурой.
# Отдельно параметр default используется для возврата значения, если на вход передана пустой итератор.

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))


# min(iterable, *[, key, default]) или min(arg1, arg2, *args[, key])
# Функция работает аналогично max, но ищет минимальный элемент.

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",
109_000)]
print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))


# sum(iterable, /, start=0)
# Функция принимает объект итератор и подсчитывает сумму всех элементов. Ключевой аргумент start задаёт начальное значение для суммирования.

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024)) # Итоговую сумму сложи со значение start


'''
Функции all(), any()
'''


# all(iterable)
# Функция возвращает истину, если все элементы последовательности являются истиной. На Python создание функции all выглядело бы так:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# Функция all обычно применяется с результатами каких-то вычислений, которые должны быть истинными или ложными.

numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')


# any(iterable)
# Функция возвращает истину, если хотя бы один элемент последовательности являются истиной. На Python создание функции any выглядело бы так:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# Функция any работает аналогично all. Но если all можно представить как if c цепочкой and, то any — это if с цепочкой or.
# Функция map заменила числа на True и False, далее all проверила все ли элементы больше нуля или есть как минимум один не более нуля.

numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')


'''
Функции chr(), ord()
'''

# chr(integer)
# Функция возвращает строковой символ из таблицы Юникод по его номеру. Номер - целое число от 0 до 1_114_111.

print(chr(97))
print(chr(1105))
print(chr(128519))


# ord(char)
# Функция принимает один символ и возвращает его код в таблице Юникод.

print(ord('a'))
print(ord('а'))
print(ord('😉'))

# Функции ord и chr выполняют противоположные действия


'''
Функции locals(), globals(), vars()
'''

# Функция locals()
# Функция возвращает словарь переменных из локальной области видимости на момент вызова функции.

SIZE = 10

def func(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return z

func(1, 2, 3)


# Функция globals()
# Функция возвращает словарь переменных из глобальной области видимости, т.е. из пространства модуля

SIZE = 10

def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z

print(globals())
print(func(1, 2, 3))

# Функция не сохраняет в словаре локальные переменные функций, даже если будет вызвана из тела функции.
# В словаре от globals содержаться и дандер переменные модуля. Они нужны Python для правильной работы кода.

# Внимание! Если вызвать функцию locals() из основного кода модуля, а не из функции, результат будет аналогичен работе функции globals()

x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(x)

# Функция vars()
# Функция без аргументов работает аналогично функции locals(). Если передать в vars объект, функция возвращает его атрибут __dict__.
# А если такого атрибута нет у объекта, вызывает ошибку TypeError.

print(vars(int)) # Получили все дандер методы класса int

