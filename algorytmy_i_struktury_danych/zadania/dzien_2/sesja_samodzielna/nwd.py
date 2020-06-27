"""
    NWD rekurencyjnie
"""


def nwd(a, b):  # 6, 6 -> 6
    if a == b:
        return a
    if a > b:
        a = a-b
    elif b > a:
        b = b-a

    return nwd(a, b)  # 6, 6


print(nwd(36, 27))
