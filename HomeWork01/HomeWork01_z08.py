a = int(input('Введите год: '))

if a % 400 == 0:
    print(a, "- високосный")
else:
    if a % 100 == 0:
        print(a, "- невисокосный")
    elif a % 4 == 0:
        print(a, "- високосный")
    else:
        print(a, "- невисокосный")