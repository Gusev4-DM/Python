'''
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
'''
tuple_obj = 1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem'

# Решение 1

dict_obj = {}

for key in tuple_obj:
    key_type = type(key)
    list_value = []
    for value in tuple_obj:
        if type(value) == key_type:
            list_value.append(value)
    dict_obj[key_type] = list_value

print(dict_obj)

# Решение 2

dict_obj = {}

for item in tuple_obj:
    dict_obj.setdefault(type(item), []).append(item)

print(dict_obj)

