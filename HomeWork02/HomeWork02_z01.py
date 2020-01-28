"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа
'0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать
пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

"""

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
sign = str(input("Введите знак операции между числами ('+', '-', '*', '/') или q для выхода: "))

while True:
    if sign == "q":
        print("Конец.")
        exit()
    else:
        while not (sign == "+" or sign == "-" or sign == "*" or sign == "/"):
            print("Вы ввели некорректный знак операции: %s" % sign)
            sign = str(input("Введите знак операции между числами ('+', '-', '*', '/') или q для выхода: "))
            if sign == "q":
                print("Конец.")
                exit()
        if sign == "+":
            result = a + b
        elif sign == "-":
            result = a - b
        elif sign == "*":
            result = a * b
        else:
            if b == 0:
                result = "на ноль делить нельзя"
            else:
                result = a / b
        print(a, sign, b, "=", result)
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        sign = str(input("Введите знак операции между числами ('+', '-', '*', '/') или q для выхода: "))
