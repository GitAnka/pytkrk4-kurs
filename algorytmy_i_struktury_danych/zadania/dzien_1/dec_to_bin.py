"""
    zamiana liczby dziesietnej na binarna
"""

def dec_to_bin(d: int) -> str:

    binary_str = ''

    while d != 0:
        r = d % 2

        if r == 1:
            binary_str = '1' + binary_str
        else:
            binary_str = '0' + binary_str

        d = d//2

    return binary_str


print(dec_to_bin(4))