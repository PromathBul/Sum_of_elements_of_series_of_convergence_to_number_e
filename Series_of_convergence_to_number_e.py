number_n = int(input('Введите число n: '))
sum = 0
for i in range(1, number_n + 1):
    sum += (1 + 1 / i) ** i
print(f'Сумма последовательности из {number_n} чисел равна {sum}')