"""
    sortowanie szybkie - implementacja
"""

def qs(t: list):
    def quick_sort(t: list, L: int, P: int):
        i = L
        j = P
        x = t[(L + P) // 2]

        while i < j:

            while t[i] < x:
                i += 1

            while x < t[j]:
                j -= 1

            if i <= j:
                t[i], t[j] = t[j], t[i]
                i += 1
                j -= 1

            if L < j:
                quick_sort(t, L, j)
            if i < P:
                quick_sort(t, i, P)

    L = 0
    P = len(t)-1

    quick_sort(t, L, P)


a = [5,7,3,2,6,9,1,0]
qs(a)
print(a)
