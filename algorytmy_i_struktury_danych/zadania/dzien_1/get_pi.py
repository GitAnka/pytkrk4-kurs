"""
    funkcja wyliczajaca wartosc liczby pi
"""

import random
import math


def get_pi():

    a, b, r = 1, 1, 1
    circle_points = 0
    square_points = 0

    for _ in range(10000000):

        x = random.random() * 2  # real number 0-1 -> 0-2
        y = random.random() * 2

        if (x-a)**2 + (y-b)**2 <= r**2:
            circle_points += 1
        #     square_points += 1
        # else:
        #     square_points += 1
        square_points += 1

    return 4 * circle_points/square_points


print(get_pi())
print(math.pi)
