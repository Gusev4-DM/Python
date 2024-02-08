'''
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
'''

my_list = [1, 2, 3, 2, 4, 5, 3, 6, 6,]

# Решение 1

unique_list = [item for item in my_list if my_list.count(item) != 2]

print(unique_list)
