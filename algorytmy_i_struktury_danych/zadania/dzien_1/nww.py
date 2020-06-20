"""
    obliczanie najmniejszej wspolnej wielokrotnosci
"""


def nww(m: int, n: int) -> int:

    c = m*n

    while m != n:  # m == n True
        if m > n:
            m = m-n  # m -= n
        else:
            n = n-m  # n -=m

    NWW = int(c/n)

    return NWW


print(nww(8, 6))
