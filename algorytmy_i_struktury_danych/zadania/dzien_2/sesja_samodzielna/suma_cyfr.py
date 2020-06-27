"""
    obliczanie sumy cyfr w sposob rekurencyjny
"""


def count_digit_sum(num):
    digits_sum = 0
    digits_sum += digits_sum % 10
    num = num // 10  # 12 3

    if num:  # if num -> False
        return digits_sum + count_digit_sum(num)
    else:
        return digits_sum


print(count_digit_sum(345))
