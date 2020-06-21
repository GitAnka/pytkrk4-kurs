"""
    obliczanie ciagu fibonacciego rekurencyjnie i iteracyjnie
"""

import time


def fibo_iter(n):
    a, b = 0, 1
    # a = 0
    # b = 1
    for _ in range(n):  # range(5) -> 0,1,2,3,4
        a, b = b, a+b
    return a


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

a = time.perf_counter()  # time.time()
print(fibo_iter(20))  # 0,1,1,2,3,5
b = time.perf_counter()
print(fibo(20))
c = time.perf_counter()
print(f'Czas dla iter: {b-a}, a czas dla rek: {c-b}')



