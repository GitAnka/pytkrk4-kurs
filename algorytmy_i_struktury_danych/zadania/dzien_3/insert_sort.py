"""
    algorytm sortowania przez wstawianie
"""


def insort_sort(d: list) -> None:
    n = len(d) - 1
    j = n - 1

    while j >= 0:
        x = d[j]
        i = j + 1

        while i <= n:
            if x <= d[i]:
                break
            else:
                d[i-1] = d[i]
                i += 1
        d[i-1] = x
        j = j - 1

        # return None

import random
b = list(range(10000))
random.shuffle(b)
a = [2,0,1,3,8,7,1,1,6]
insort_sort(a)  #
insort_sort(b)

print(a)
print(b)
