"""NOTE Revisiting Recursion NOTE"""
# start by writing a factorial recursion...
def factorial(n): 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# you don't even need a while loop. this is how recursion works!

def fibonacci(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# honestly, just do more practice problems on reading and writing recursive algorithms.
