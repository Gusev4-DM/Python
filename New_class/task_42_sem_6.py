'''
1. Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
2. Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
3. Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
4. Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
5. Проверку года на високосность вынести в отдельную
защищённую функцию.
'''

__all__ = ['some_func', 'data'] # Таким образом мы защищаем функцию от импорта, прописывая какие функции берем в импорт в переменной __all__ 

data = '01.02.2026'


def _leap_year(year):

    """
    Знак'_' перед названием функции указывает на ее защищенность 
    Если мы будем импортировать ее обращаясь к ней то она импортируется from task_42_sem_6.py import _leap_year
    Если мы будем импортировть весь модуль например from task_42_sem_6.py import *, то она не импортируется
    """

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'Год високосный')
        return False
    else:
        print(f'Год не високосный')
        return True


def some_func(data):
    day, month, year = [int(i) for i in data.split('.')]

    if year > 9999 or month > 12:
        return False
    
    month_30 = (4, 6, 9, 11)
    month_31 = (1, 3, 5, 7, 8, 10, 12)

    if month in month_30:
        if 0 < day < 31:
            return True
        return False
    
    elif month in month_31:
        if 0 < day < 32:
            return True
        return False
    
    elif month == 2:
        if _leap_year(year):
            if 0 < day < 29:
                return True
            return False
        
        else:
            if 0 < day < 30:
                return True
            return False
            

print(some_func(data))