"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
массив, элементы которого это цифры числа.

Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
from collections import deque

hex_to_dec = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
              "D": 13, "E": 14, "F": 15}

dec_to_hex = {v: k for k, v in hex_to_dec.items()}


def hex_sum(val1, val2, prev_to_mind="0"):
    val1_dec = hex_to_dec[val1]
    val2_dec = hex_to_dec[val2]
    sum_val = val1_dec + val2_dec + hex_to_dec[prev_to_mind]
    return dec_to_hex[sum_val % 16], dec_to_hex[sum_val // 16]


def hex_mul(val1, val2, prev_to_mind="0"):
    val1_dec = hex_to_dec[val1]
    val2_dec = hex_to_dec[val2]
    mul_val = val1_dec * val2_dec + hex_to_dec[prev_to_mind]
    return dec_to_hex[mul_val % 16], dec_to_hex[mul_val // 16]


def mul_1hex_to_list(list1, hex1):
    deq1 = deque(list1)
    res_deq = deque()

    deq1_len = len(deq1)
    to_mind = "0"
    for i in range(deq1_len):
        val1 = deq1.pop()
        res_tmp = hex_mul(val1, hex1, to_mind)
        to_mind = res_tmp[1]
        res_deq.appendleft(res_tmp[0])
    if to_mind != "0":
        res_deq.appendleft(to_mind)
    return res_deq