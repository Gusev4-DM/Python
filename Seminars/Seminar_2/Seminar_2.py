
# Задача 1. Написать множество чисел от 1 до n при вводе n. Например: 5 = 1*2*3*4*5 = 120


n = int(input('Введите число от 1 до 5: '))

fact = 1
while n > 0:
    fact *= n
    n -= 1

print(fact)


# Задача 2. Написать номер числа фибоначи например Ввод 5 = 6


n = int(input('Введите номер числа фибоначи: '))

n_1, n_2 = 0, 1 # 0 1 1 2 3 5 8 13
fib = 2
while n_2 < n:
    n_1, n_2 = n_2, n_1 + n_2 # меняет местами Н_1 и Н_2 на Н_2 и Н_1 + Н_2
    fib += 1
if n != n_2:
    fib = -1
print(fib)


# Задача 3. input 6 -> -20 30 -40 50 10 -10, output = 2


n = int(input('Ведите количество дней N: '))

k = 0
numbers = 0

for i in range(n):
    temp = int(input('Введите температуру: '))
    if temp >= 0:
        k += 1
        numbers = max(numbers, k)
    else:
        k = 0

print(f'Максимальная оттепель будет составлять {numbers} дня')


# Задача 4. Максимальное и минимальное значение
    
numbers = int(input('Введите колличество арбузов: '))
weight = int(input('Введите массу этих арбузов: '))
maximum = weight
minimum = weight
for i in range(numbers - 1):
    weight = int(input('Введите массу этих арбузов: '))
    maximum = max(maximum, weight)
    minimum = min(minimum, weight)

print(f' максимум - {maximum}, минимум - {minimum}')