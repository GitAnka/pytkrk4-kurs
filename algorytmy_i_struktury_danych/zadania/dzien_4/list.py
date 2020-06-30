"""
    implementacja listy - struktura danych
"""


class Element:
    def __init__(self, data):
        self.data = data  # value
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_element(self, elem):
        # lista jest pusta -> dodajemy pierwszy element
        if self.head is None:
            self.head = elem
            self.tail = elem
        # lista nie jest pusta -> dodajemy na jej koncu
        else:
            self.tail.next = elem
            self.tail = elem
        self.count += 1

    def print_data(self):
        elem = self.head
        while True:
            print(elem.data, end=" ")
            if elem is self.tail:
                break
            elem = elem.next

my_list = List()
elem1 = Element(1)
my_list.add_element(elem1)
elem2 = Element(2)
elem3 = Element(1)
elem4 = Element(2)
my_list.add_element(elem2)
my_list.add_element(elem3)
my_list.add_element(elem4)
my_list.print_data()