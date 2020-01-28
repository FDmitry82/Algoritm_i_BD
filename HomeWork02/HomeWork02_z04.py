"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

n = int(input("Введите длину последовательности n: "))

val = 1
sum = 0

for i in range(n):
    sum += val
    val *= -0.5

print("Сумма %d элементов последовательности равна %.10f" % (n, sum))