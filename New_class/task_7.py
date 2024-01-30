'''
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные. 
'''

some_list = [1, 3.14, 'hello', None, True]

# Итератор

for i in some_list:
    print(type(i), end=' ') 

print()

# Индекс

for i in range(len(some_list)):
    print(type(some_list[i]), end=' ')


