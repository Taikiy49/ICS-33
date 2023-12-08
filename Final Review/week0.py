"""NOTE CLASSES AND OBJECTS NOTE"""

def try_kwargs(**kwargs):  # puts it in a dictionary
    for key, value in kwargs.items():
        return key, value


def try_args(*args):
    for arg in args:
        return arg


def try_both(*args, **kwargs):
    if args:
        return args
    if kwargs:
        return kwargs


if __name__ == "__main__":
    """kwargs ONLY takes keyword arguments, while args takes in ONLY positional arguments."""
    try_kwargs(age=5, name='Taiki')
    try_args(1, 2, 3)
    """What about both?"""
    try_both(5, 3, 5)
    try_both(name="taiki", age=3)
    try_both(18, 2004, name="taiki")
    """ABOVE works, but make sure positional arguments go before keyword arguments."""
#
# """How do I write unit tests again?"""
# import unittest
#
# """realize that unittest.TestCase is a class inheritance?!"""
# class PracticeUnitTest(unittest.TestCase):
#     def test_idk(self):
#         self.assertEqual(bool([]), False)
#
#     def test_store_print(self):
#         import contextlib
#         import io
#         with contextlib.redirect_stdout(io.StringIO()) as output:
#             print(try_kwargs(a=1, b=3))
#         self.assertEqual(output.getvalue(), f"('a', 1)\n")
#

def square(n):
    return n * n

#
# if __name__ == "__main__":
#     print(list(range(5)))
#     print(__builtins__.dict(a=3, b=4, c=3))
#     """woh that's actually kinda cool"""
#     print(square(3))
#     print(dir())
#     """AND it's added to the directory! What if..."""
#     square5 = square(5)
#     print(dir())
#     """SQUARE5 IS ALSO ADDED TO THE DIRECTORY!"""

"""CLASSES AND OBJECTS"""
# class Exponent:
#     def square(self, n):
#         return n * n
#     def cube(self, n):
#         return n * n * n
# 
# exponent = Exponent()
# square2 = exponent.square(2)
# 

# class StaticMethod:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @staticmethod
#     def compute():
#         return "Static method called."

# if __name__ == "__main__":
#     static_method = StaticMethod('Taiki', 19)
#     print(static_method.name, static_method.age)
#     print(static_method.compute())


class UseStaticMethod:
    def __init__(self, my_list):
        self.my_list = my_list

    @staticmethod
    def check_true(lst):
        if lst:
            return True
        else:
            return False

if __name__ == "__main__":
    use_static_method = UseStaticMethod([1, 2, 3])
    print(use_static_method.check_true([1]))
    print(use_static_method.check_true([]))
    print(use_static_method.my_list)
