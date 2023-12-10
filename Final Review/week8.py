
"""NOTE Functional Programming NOTE"""
# INTRODUCING lambda
square = lambda n: n * n
(square(3)) # output: 9 

# more uses for this useful lambda!
make_revesed_list = lambda *values: list(reversed(values))
make_dict = lambda **kwargs: dict(kwargs)

"""Now let's take a look at higher order functions!"""
def square(n):
    return n * n
def transform_all(f, values):
    for value in values:
        yield f(value)

(list(transform_all(square, [1, 2, 3]))) # output: [1, 4, 9]
# very cool, now can we implement lambda somewhere?
(list(transform_all(lambda n: n * 10, [1, 2, 4]))) # output: [10, 20, 40]

"""Now the real deal... Fuctions that return other functions!"""
def make_function():
    def another_function():
        return "Hello Boo!"
    return another_function

(make_function()) # output: <function blah blah>
(make_function()()) # output: Hello Boo!
# Also, if I try to call another_function, it will cause an error...

"""Lets look at another example..."""
def negate(f):
    def execute(n):
        return not f(n)
    return execute

none = negate(any)
(none(x < 0 for x in [1, 2, 3, 4])) # basically, it means... all values are greater than 0

def negate(f):
    return lambda n: not f(n)
# this could've been another way to write your function...

def compose(f, g):
    def execute(n):
        return f(g(n))
    return execute
# woh that's very cool, a function inside another function

square_times_two = compose(lambda n: n * 2, lambda n: n * n)
# print(square_times_two(5)) # output: 50
finding_length = compose(len, str)
# print(finding_length(5123131)) # output: 7
# awesome!

def make_pipeline(first, *everything):
    def execute_pipeline(n):
        current = first(n)
        for f in everything:
            current = f(current)
        return current 
    return execute_pipeline

do_something = make_pipeline(int, lambda n: n * 3, lambda n: n + 3, lambda n: n // 2)

"""Partially calling functions!"""
def multiply(n, m):
    return n * m 
def partially_call(f, n):
    def complete(m):
        return f(n, m)
    return complete

multiply_by_three = partially_call(multiply, 3)
# print(multiply_by_three(5))

"""Lets now create a partially call with an inifinite amount of arguments..."""
def partially_call(f, *args):
    def complete(*remaining_args):
        return f(*args, *remaining_args)
    return complete

print_description = partially_call(print, 'How', 'is', 'Boo', 'today')
# print(print_description('Boo', 'is', 'doing', 'great', 'today!'))
# output: How is Boo today Boo is doing great today!

"""Lets look at another exmample that uses map and filter for higher order functions"""
(list(map(lambda a, b, c: a + b * c, [1, 3, 5], [2, 4, 8], [-1, 1, -1])))
# output: [-1, 7, -3]
(list(map(lambda a, b: a ** b, [1, 2, 3], [4, 5])))
# output: [1, 32]
# notice that the 5 is completely ignored. Once one iterable runs out of elements, the output stops there...

"""Let's say we have a function..."""
def is_positive(n):
    return n > 0

(list(filter(is_positive, [1, -2, 3, -4, 5, -7]))) # output: [1, 3, 5]
(list(filter(negate(is_positive), [1, 2, 3, 4, -5, -6]))) # output: [-5, -6]
(list(filter(negate(is_positive), [1, 2, 3, -3, -7, -9]))) # output: [-3, -7, -9]

"""INTRODUCING functools"""
import functools
# functools.reduce() -> reduce basically slams everything together...

(functools.reduce(lambda a, b: a + b, [1, 2, 3, 4])) # output: 10
(functools.reduce(lambda a, b: a + b, [[1, 2], [3, 4], [5, 6]])) # output: [1, 2, 3, 4, 5, 6]
(functools.reduce(max, [1, 2, 11, 7, 6])) # output: 11

import operator
(functools.reduce(operator.add, [1, 2, 3])) # output: 6
(functools.reduce(operator.mul, [1, 2, 3], [4, 5, 6])) # output: [4, 10, 18]
(list(filter(operator.truth, [-3, -2, -1, 0, 1, 2, 3]))) # output: [-3, -2, -1, 1, 2, 3]
(list(filter(negate(operator.truth), [-3, -2, -1, 0, 1, 2, 3]))) # output: [0]

def square(n):
    return n * n

"""INTRODUCING the __call__ dunder method!"""

class Square:
    def __call__(self, n):
        return n * n

square = Square()

"""now lets create your own class that is callable!"""
class Callable:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __call__(self):
        return name, age

class NotCallable:
    def __init__(self, name, age):
        self._name = name
        self._age = age

call = Callable('taiki', 19)
noncall = NotCallable('taiki', 19)

(callable(call)) # callable because a call method exists...
(callable(noncall)) # not callable because a call method does not exist...





