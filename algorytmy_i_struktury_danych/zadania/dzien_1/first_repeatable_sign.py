"""
    Zawiera funkcje znajdujaca pierwszy powtarzajacy sie znak w napisie.
"""


def find_first_repeatable_sign(string: str) -> str:

    temp = set()  # temp = []

    for sign in string:  # string = "kajak", sign = "k"
        if sign not in temp:
            temp.add(sign)
        else:
            return sign

    # return None


print(find_first_repeatable_sign("abcdef"))


