'''
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''

names = ['Alex', 'Nick', 'Michael']
count = 1
tapes = 1500
txt = 'Test'
rows = 'first'
s = -15
sym_calls = True

var = globals().copy()

var_new = {}

for key in var:
    if not key.startswith('__'):
        var_new[key] = var[key]
    
print(var_new)

for key in var_new.copy():
    if key.endswith('s') and len(key) != 1:
        var_new[key[:-1]] = var_new[key]
        var_new[key] = None

print(var_new)

