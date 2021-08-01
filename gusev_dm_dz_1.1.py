sec = int(input('Введите число в секундах: '))
day = sec // 86400
sec = sec % (24 * 3600)
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print(f'у вас {day} дней, {hour} час, {min} мин, и {sec} сек.')
