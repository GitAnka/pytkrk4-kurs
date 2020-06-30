"""
    wlasna implementacja copy slownika
"""

class SuperLista(list):
    ...

def dict_copy(d1: dict) -> dict:
    copy_dict = {}
    for key, value in d1.items():  # d1 = {'a':1, 'b':2} -> [('a',1), ('b', 2)]
        if isinstance(value, list):  # type(value) == list
            new_value = value[:]
        copy_dict[key] = new_value
    return copy_dict
    # return dict(d1)  # -> dict(d1)
    # return {key: value for key, value in d1.items()}


d1 = {'a': [1], 'b': [2]}
d2 = dict_copy(d1)
d3 = d2.copy()
d1['a'].append(2)  # d1 -> {'a':[1,2], 'b': [2]}
print(d2)
print(d3)
