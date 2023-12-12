class X:
    def only_x(self):
        print('only X')
    def both(self):
        print('both X')
class Y:
    def only_y(self):
        print('only Y')
    def both(self):
        print('both Y')
class Z(X, Y):
    def only_x(self):
        super().only_x()
    def only_y(self):
        super().only_y()
    def both(self):
        super().both()

z = Z()
# (z.both()) # output: both X
# reasonable theory is that X is listed first in Z's bases, so it wins!

class W:
    def foo(self):
        print('W foo')
class X(W):
    def foo(self):
        print('X foo')
        super().foo()
class Y(W):
    def foo(self):
        print('Y foo')
        super().foo()
class Z(X, Y):
    def print(self):
        print('Z foo')
        super().foo()

# X().foo()
# Y().foo()
# Z().foo() # this is very interesting, X foo called Y foo even though Y is not X's base class. 

"""NOTE (2) NOTE"""
class HashableByAttributes:
    def __hash__(self):
        return hash((self._name, self._age))
    def __eq__(self, other):
        if type(self) is type(other):
            return self._name == other._name and self._age == other._age

class Person(HashableByAttributes):
    def __init__(self, name, age):
        self._name = name
        self._age = age 

(hash(Person('Boo', 13)) == hash(Person('Boo', 13))) # output: True
(hash(Person('Boo', 15)) == hash(Person('Boo', 13))) # output: False
(Person('Boo', 13) == Person('Boo', 13)) # output: True
(Person('Boo', 13) == Person('Boo', 15)) # output: False

"""NOTE (3) NOTE"""

def sequential_search(collection, search_key):
    def search_from(iterator, key):
        try:
            element = next(iterator)
            if element == key:
                return True
            else:
                return search_from(iterator, key)

        except StopIteration:
            return False
    return search_from(iter(items), key)


def binary_search(collection, search_key):
    def search_in(items, start, end, search_key):
        if start > end:
            return False
        middle = (start + end) // 2

        if items[middle] == key:
            return True
        elif items[middle] < key:
            start = middle + 1
        else:
            start = middle - 1
        return search_in(items, start, end, key)
    return search_in(items, 0, len(items), key)

"""NOTE (4) NOTE"""
def square(n):
    return n * n

def make_repeater(f, count):
    def execute_repeater(initial):
        current = initial
        for _ in range(count):
            current = f(current)
        return current
    return execute_repeater


"""Cool that was a bit tough..."""
# here, lets create another one!

def cube(n):
    return n * n * n

def repeater(f, count):
    def execute_repeater(initial):
        value = initial
        for _ in range(count):
            value = f(value)
            print(value)
        return value
    return execute_add


def square(n):
    return n * n

def make_repeater(f, count):
    def execute_repeater(initial):
        current = initial
        for _ in range(count):
            current = f(current)
        return current
    return execute_repeater

a = make_repeater(square, 2)
print(a(3))






    

