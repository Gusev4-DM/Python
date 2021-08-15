def old_nums(number):
    for num in range(1, number + 1):
        yield num


number = int(input('Введите число: '))
num_gen = old_nums(number)
print(list(num_gen))

# без функции yield

num_gen_2 = (num for num in range(1, number + 1))
print(list(num_gen_2))
