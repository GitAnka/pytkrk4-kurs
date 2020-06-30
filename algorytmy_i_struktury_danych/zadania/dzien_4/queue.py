"""
    prosta implementacja kolejki
"""

from collections import deque


class FifoQueue:

    def __init__(self):
        self.data = deque()
        self.length = 0

    def append(self, element):
        self.data.appendleft(element)
        self.length += 1

    def pop(self):
        if self.length != 0:
            self.length -= 1
            return self.data.pop()
        else:
            return "KOLEJKA JEST PUSTA!"

    def print(self):
        print(list(self.data))


my_queue = FifoQueue()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
my_queue.print()
my_queue.pop()
my_queue.print()
my_queue.append(1)
my_queue.print()