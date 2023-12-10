"""NOTE Decorators NOTE"""
# a decorator is a function that accepts a callable argument and returns a function as its result.
# for example, this is a decorator that won't change the function whatsoever...
def unchanged(func): # make sure if you want to use something as a decorator it has the "func"
                     # as an argument
    return func

@unchanged
def square(n):
    return n * n

def with_greeting(func):
    def greet_and_execute(n):
        print("Boo!")
        return func(n)
    return greet_and_execute

def with_greeting2(func):
    def greet_and_execute(n):
        print("Hello")
        return func(n)
    return greet_and_execute

@with_greeting2
@with_greeting
def square(n):
    return n * n

# print(square(3))

"""Now there's an issue... If multiply we have two arguments..."""
@with_greeting
def multiply(n, m):
    return n * m 

# (multiply(6, 17)) # this will cause an error because greet_and_execute takes 
                    # 1 positional argument but 2 were given...

import math 

def with_greeting(func):
    def greet_and_execute(*args, **kwargs):  # this way, it can take an infinite amount of arguments.
        print("Hello!")
        return func(*args, **kwargs)
    return greet_and_execute

@with_greeting
def distance_from_origin(x, y, z = 0):
    return math.hypot(x, y, z)

@with_greeting
def multiply(n, m):
    return n * m
 
# (distance_from_origin(3, 4)) # output: Hello!, 5.0
# (multiply(2, 3)) # output: Hello!, 6
# (multiply(5, 7)) # output: Hello!, 35


"""now lets take a look at this..."""
def read_int():
    for _ in range(4):
        try:
            return int(input("Enter an integer: "))
        except Exception:
            pass
    return int(input("Enter an integer: "))

"""we can do this in a more simpler fashion by using decorators!
   it would prolly look something like this...
""" 
def retry_on_failure(times): # notice that it takes the number of times in the first function and not "func"
    def decorate(func): # notice that now the func argument is passed in a function inside the other first function.
        def run(*args, **kwargs):
            for _ in range(times - 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            return func(*args, **kwargs)
        return run
    return decorate

def retry_on_failure_once(func):
    def run(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            pass
        return func(*args, **kwargs)
    return run

@retry_on_failure_once
def read_int():
    return int(input("Enter an integer: ")) 

# print(read_int())
 
@retry_on_failure(3)
def read_int():
    return int(input("Enter an integer: "))

# print(read_int())

def bad_idea(func):
    return 'Boo!'

# @bad_idea # this will not work because a str object is not callable! 
          # you can put () for stuff that you can call in python...
def square(n):
    return n * name

"""now lets look at decorators for classes!"""
class InterestingIdea:
    def __init__(self, func): # notice that the func argument is in the __init__ method...
        pass
    def __call__(self, *args, **kwargs): # this will make it callable. you can also return what you want...
        return 'Boo!'

@InterestingIdea
def square(n):
    return n * n
# output: Boo!

class WithCallsCounted:
    def __init__(self, func):
        self._func = func
        self._count = 0
    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._func(*args, **kwargs)
    def count(self):
        return self._count

@WithCallsCounted
def square(n):
    return n * n

(square(3)) # output: 9
(square.count()) # output: 1
(square(5)) # output: 25
(square.count()) # output: 2

"""Lets look at an example with cls!"""
def booize(cls):
    return 'Boo!'

@booize
class Another:
    pass

(Another) # Boo!

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def name(self):
        return self._name
    def age(self):
        return self._age

def fields(field_names):
    field_names = list(field_names)

    def make_field_getter(field_name):
        def get_field(self):
            return getattr(self, field_name)
        return get_field
    
    def decorate(cls):
        for field_name in field_names:
            setattr(cls, field_name, make_field_getter(field_name))
        
        def __init__(self, *args):
            for field_name, arg in zip(field_names, args):
                setattr(self, field_name, arg)
        
        cls.__init__ = __init__
        return cls
    return decorate

"""What about decorating methods in classes?"""

class AlwaysBoo:
    def __get__(self, obj, objtype):
        return 'Boo!'

class HashBoo:
    boo = AlwaysBoo()

x = HashBoo() 
(x.boo) # output: Boo!
# whatever __get__ returns becomes the value we get back when accessing the attribute.

"""Lets try another class that uses __get__"""
class Pokemon:
    def __get__(self, obj, objtype):
        return "Charizard"
class Charizard:
    pokemon = Pokemon()

charizard = Charizard()
(charizard.pokemon) # output: Charizard

"""now... lets make the WithCallsCounted more advanced..."""
class WithCallsCounted:
    def __init__(self, func):
        self._func = func
        self._count = 0

    def _call_original(self, func, *args, **kwargs):
        self._count += 1
        return func(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self._call_original(self._func, *args, **kwargs)

    def __get__(self, obj, objtype):
        def execute(*args, **kwargs):
            original_func = self._func.__get__(obj, objtype)
            return self._call_original(original_func, *args, **kwargs)
        
        execute.count = self.count
        return execute
    
    def count(self):
        return self._count
    
@WithCallsCounted
def square(n):
    return n * n

class Thing:
    @WithCallsCounted
    def value(self):
        return 13

(square(3))
(square.count())
t1 = Thing()
t2 = Thing()
(t1.value())
(t1.value.count())
(Thing.value(t1))
(t2.value.count())
(Thing.value.count())
 
"""basically, the WithCallsCounted decorator counts the amount of times the objects has been called?
   most importantly, we have to know _call_original initializes adds to the count and initializes which function
   it takes. the __call__ method ensures that the object is callable. the __get__ method is used to access
   attributes from a class... very confusing...
"""

"""INTRODUCING caching!"""
import functools
@functools.cache
def square(n):
    print(f"Calculating square of {n}...")
    return n * n

# (square(3)) # output: Calculating square of 3..., 9
# (square(3)) # output: 9

@functools.cache
def fast_fibonacci(n):
    return n if n < 2 else fast_fibonacci(n - 1) + fast_fibonacci(n - 2)

(fast_fibonacci(300))  # without caching, it won't even output anything because it takes too many recursive steps...

# there are also a couple more functools...
@lru_cache # last recently used cache, whatever that means lol
@functools.total_ordering # used when decorating classes that contain __eq__ and __lt__ methods...
                          # it implements the remaining methods according to the pattern similar to the one
                          # described below so that we don't have to...
class Thing:
    pass
    
""" 

__ne__ could return the negation of what __eq__ returns
__ge__ could return the negation of what __lt__ returns
__le__ could use __eq__ and __lt__ and combine their results
__gt__ could return the negation of what our automatically-generated __le__ return 

"""

