"""
    silnia z wykorzystaniem podejscia programowania dynamicznego
"""


def silnia(n, cache={}):
    print(cache)
    if n in cache:
        return cache[n]
    if n in (0, 1):
        return 1
    else:
        cache[n] = n*silnia(n-1)
        return cache[n]

print(silnia(5))
print(silnia(8))  # 499 ---> 1
print(silnia(10))
