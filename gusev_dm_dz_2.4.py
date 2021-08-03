raw_message = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
message = ' '.join(raw_message)
new_message = message.split()
print('Привет', new_message[1].capitalize())
print('Привет', new_message[4].capitalize())
print('Привет', new_message[8].capitalize())
print('Привет', new_message[10].capitalize())