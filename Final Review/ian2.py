"""make me a four index..."""
# for a sequence, you only need getiitem and len...

class FourSequence:
    def __len__(self):
        return 4
    def __getitem__(self, index):
        return index * 4

"""build me an inheritance class!"""
class Eevee:
    def value(self):
        return 'water'

class Vaporeon(Eevee):
    def __init__(self, level):
        self._level = level
    def pokemon_type(self):
        return super().value()
    def pokemon_level(self):
        return self._level


v = Vaporeon(15)
(v.pokemon_type())
(v.pokemon_level())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def make_pipeline(first, *everything):
    def execute_pipeline(n):
        current = first(n)
        for f in everything:
            current = f(current)
        return current 
    return execute_pipeline









do_something = make_pipeline(int, lambda n: n * 3, lambda n: n + 3, lambda n: n // 2)
do_something(5) # 9


def make_pipeline(first, *args):
    def execute_pipeline(n):
        current = first(n)
        for f in args:
            current = f(current)
        return current
    return execute_pipeline

do_something = make_pipeline(int, lambda n: n * 3, lambda n: n + 3, lambda n: n // 2)
(do_something(5))


def partially_call(f, *args):
    def execute_partially_call(*rest):
        value = f(*args, *rest)
        return value
    return execute_partially_call

p = partially_call(max, 1, 2, 3)
# print(p(4, 5, 6)

"""now, let's try to use property and value.setter"""
class Thing:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    


