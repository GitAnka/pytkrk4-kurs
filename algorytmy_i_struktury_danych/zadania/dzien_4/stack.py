"""
    wlasna implementacja stosu
"""


class Stack:
    def __init__(self, limit: int = None):
        self.data = []
        self.length = 0
        self.limit = limit

    def push(self, element: int):
        if self.limit is None or self.length < self.limit:
            self.data.append(element)
            self.length += 1
        else:
            print("STOS JEST PELNY")

    def pop(self):
        if self.length != 0:
            self.length -= 1
            return self.data.pop()
        else:
            return "STOS JEST PUSTY"


my_stack = Stack(limit=5)
print(my_stack.data)  # []
my_stack.push(1)  # [1]; jezeli limit bylby przekroczony - STOS JEST PELNY
print(my_stack.data)  # [1]
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.data)
my_stack.push(1)
print(my_stack.data)
my_stack.push(1)
print(my_stack.data)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
