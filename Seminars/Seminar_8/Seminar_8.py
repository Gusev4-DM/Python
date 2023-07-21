'''
f = open('file.txt', 'r')
data = f.read()
print(data)
f.close()

with open('file.txt', 'r', encoding='utf8') as f: # 'r' - читать
    data = f.readlines() # f.read()
    data = list(map(str.strip, data))
    print(data)

sp = ['567', '888']
with open('file.txt', 'a', encoding='utf8') as f: # 'a' - запись
    f.writelines(sp)
    print(sp)

sp = ['567\n', '888']
with open('file.txt', 'w', encoding='utf8') as f: # 'w' - перезапись
    f.writelines(sp)
'''

'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt Фамилия, имя, отчество, номер телефона - данные. Которые должны находиться в файле.
1. Программа должна вводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одно из полей (например имя или фамилию)
4. Использование функций. Программа не должна быть линейной
'''


def show_all_records():
    with open('file.txt', 'r', encoding='utf8') as f:
        data = []
        for i in f:
            data.append(i.strip().replace(';', ' '))
        
        print('\nПолный список справочника.')

        count = 0
        for i in data:
            count += 1
            print(f'{count}. {i}')


def search_record(name):
    with open('file.txt', 'r', encoding='utf8') as f:
        data = []
        for i in f:
            data.append(i.strip().replace(';', ' '))

        print(*list(filter(lambda x: name in x, data)))
            
                
def add_contact():
    with open('file.txt', 'a', encoding='utf8') as f:
        f.write('\n')
        f.write(input('Введите ФИО с номером телефона через пробел: ').replace(' ', ';'),)
        print('Данные успешно внесены.')


def delete_record(user_deleted):

    not_find_flag = True

    with open('file.txt', 'r', encoding='utf8') as f:
        data = []
        for i in f:
            data.append(i.strip().replace(';', ' '))

        for i in data:
            if user_deleted in i:
                data.remove(i)
                not_find_flag = False

        data = ('\n'.join(data))


    if not_find_flag:
        print(f'Значение {user_deleted} не найдено.')
        return
    
    answer = input(f'Вы подтверждаете удаление контакта {user_deleted}? (Y/N): ')
    if answer == 'Y' or answer == 'y':
        with open('file.txt', 'w', encoding='utf8') as f:
            f.write(data)
        print('Изменения сохранены.')
    else:
        print('Удаление отменено.')


def main():
    select = int(input('Выберите действие.\n'
        '1 - Показать справочник\n'
        '2 - Найти контакт\n'
        '3 - Добавить контакт\n'
        '4 - Удалить контакт\n'
        'Ввод: '))

    if select == 1:
        show_all_records()
    elif select == 2:
        name = input('Введите Фамилию: ').capitalize()
        search_record(name)
    elif select == 3:
        add_contact()
    elif select == 4:
        user_deleted = input('Введите номер телефона контакта который хотите удалить: ')
        delete_record(user_deleted)


main()