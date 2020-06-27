"""
    implementacja algorytmu babelkowego
"""

import random


def bubble_sort(t: list) -> None:
    n = len(t) - 1  # n wskazuje na ostatni indeks

    while n > 0:
        for i in range(n):
            if t[i] > t[i+1]:
                # bufor = t[i+1]
                # t[i+1] = t[i]
                # t[i] = bufor
                t[i], t[i+1] = t[i+1], t[i]
        n = n - 1  # n -= 1
    # return None


n = [4, 7, 2, 9, 5, 0]
bubble_sort(n)
m = list(range(10000))
random.shuffle(m)
print(m)
bubble_sort(m)
print(n)  # [0, 2, 4, 5, 7, 9]
print(m)
