"""NOTE (1) NOTE"""

def multiply(n, m):
    return n * m

def partially_call(f, *args, **kwargs):
    def execute_partially_call(*args, **kwargs):
        current = 1
        for arg in args:
            current = f(current, arg)
        for kwarg in kwargs.values():
            current = f(current, kwarg)
        return current
    return execute_partially_call

# p = partially_call(multiply, q=3)
# print(p(n=3, m=7))

"""NOTE (2) NOTE"""
def with_greeting(func):
    print('greetings!')
    return func

def with_boo(func):
    print('Boo!')
    return func


# @with_greeting
# @with_boo
# def square(n):
#     return n * n


# print(square(5))
"""Notice that when we have multiple decorators on the same function, it goes inwards to outwards. 
   I'm guessing this has something to do with readability? It must have something to do with the decorator
   closest to the function attached to compuetes first.
"""
        
import time

"""In this situtation, it becomes complex. The decorator has an argumnet besides func, which there should
   at least be two functions to build this algorithm. so we now have cached(size) and decorator(func) <- which
   is the argument that should be passed for functions that should be decorators. But wait... what are we going
   to do with the argument "n" from expensive_square(n)? We can't just continue with just two functions like
   how we did on other problems where it didn't matter what the input of square or other functions did. 
   This is because all we did was print something before the square or other function. This time, we have
   to access the value of n in expensive square to form our algorithm. Therefore, this becomes more complex...
"""
import functools

def cached(size):
    cached_list = []
    def decorator(func): 
        def execute(*args, **kwargs):
            for arg in args:
                try:
                    hash(arg)
                    if arg not in cached_list:
                        result = func(arg)
                        cached_list.append(arg)
                    else:
                        reuslt = func(arg)
                except TypeError:
                    pass

            for kwarg in kwargs.values():
                try: 
                    hash(kwarg)
                    if kwarg not in cached_list:
                        result = func(kwarg)
                        cached_list.append(kwarg)
                    else:
                        result = func(kwarg)
                except TypeError:
                    pass
            
            return result
        return execute
    return decorator


@cached(5)
def expensive_square(n):
    time.sleep(2)
    return n * n

"""NOTE (4) NOTE"""
# when a decorator is above a class, we can add attributes to the class, remove attributes to the class,
# and even replace the value of an attribute with a new one. Basically, any attribute that can be modified
# at all can be modified by a deocrator...

