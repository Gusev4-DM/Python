'''
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии. 
'''


def some_func(names, salaries, bonus):
    return {names: round(salaries * float(bonus.rstrip('%')) / 100, 2)
        for names, salaries, bonus in zip(names, salaries, bonus)}


names = ['Иван', 'Петр', 'Семен']
salaries = [100_000, 80_000, 115_000]
bonus = ['10.25%', '20.80%', '08.02%']

print(some_func(names, salaries, bonus))