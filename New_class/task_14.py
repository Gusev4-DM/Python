'''
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
'''
lst = ["1", "2.1", "True", "-5", "Sds"]

for item in lst:
    if item.isdigit():
        print(f'Целое число из {item}')
    else:
        try:
            print(float(item))
        except ValueError:
            print(item.lower())
