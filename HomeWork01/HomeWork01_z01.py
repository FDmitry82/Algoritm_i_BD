n = int(input('Введите трехзначное число: '))

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n % 10

print("Сумма цифр числа:", d1 + d2 + d3)
print("Произведение цифр числа:", d1 * d2 * d3)