"""
    jak najlepiej odnalezc najmniejsza liczbe z ilus podanych
"""


def find_min(a, b, c):
    if a >= b:
        if b >= c:
            return c
        else:
            return b
    else:
        if a >= c:
            return c
        else:
            return a


def find_min2(nums: list) -> int:  # [7]
    min_value = nums[0]
    for i in range(1, len(nums)):  # for num in nums[1:]:
        if min_value > nums[i]:  # if min_value > num:
            min_value = nums[i]  # min_value = num
    return min_value


print(find_min2([7,4,3]))