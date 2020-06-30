"""
    wlasna implementacja dodawania dwoch slownikow
"""


def add_dict(d1: dict, d2: dict) -> dict:
    d3 = {}
    # sposob 1
    # for key, value in d1.items():
    #     d3[key] = value
    # for key, value in d2.items():
    #     d3[key] = value
    # sposob 2
    # d3 = d1.copy()
    # d3.update(d2)
    # sposob 3
    return {**d1, **d2}  # d3
    # sposob 4 od python 3.9
    # d1 + d2 -> TAK NIE BEDZIE
    # d1 | d2

d1 = {1: 1, 2: 5}
d2 = {2: 2}
d3 = add_dict(d1, d2)  # d3 = {1:1, 2:2}