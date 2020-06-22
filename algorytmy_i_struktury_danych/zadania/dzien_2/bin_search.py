"""
    implementacja wyszukiwania binarnego
"""

import time


def bin_search(a: list, x: int) -> str:

    l = 0
    p = len(a) - 1

    while not l > p:  # l <= p

        s = (l+p)//2

        if a[s] == x:
            return f"odnaleziono element {x}, pod indeksem {s}"

        if a[s] < x:
            l = s + 1
        else:
            p = s - 1

    return f"nie odnaleziono elementu o wartosci {x}"


def find(a: list, x: int) -> str:
    for element in a:
        if element == x:
            return "znaleziono"
    return "nie znaleziono"


a = time.perf_counter()
print(bin_search([num for num in range(100000)], 99999))
b = time.perf_counter()
print(find([num for num in range(100000)], 99999))
c = time.perf_counter()
print(f"czas bin search: {b-a}, czas norm: {c-b}")