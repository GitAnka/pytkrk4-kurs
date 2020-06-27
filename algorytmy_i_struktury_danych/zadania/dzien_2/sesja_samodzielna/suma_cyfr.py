"""
    obliczanie sumy cyfr w sposob rekurencyjny
"""

def count_digit_sum(num):
    sum = 0
    sum += num % 10
    num = num // 10

    if num:
        return sum + count_digit_sum(num)
    else:
        return sum

print(count_digit_sum(345))