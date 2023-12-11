# remember * for keyword / for positional
# remember *args only takes positional argumnets and **kwargs only takes keyword arguments
"""NOTE (1) NOTE"""

def only_truthy(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        my_dict[f'_{key}'] = value
    return my_dict

"""NOTE (2) NOTE"""
# the pow method has positional only parameters defined
try:
    print(pow(2, 3))
    pow(1, b=3, c=5)
    pow(a=1, b=2, c=5)
except Exception as e:
    print(e)

# the other two methods with keyword arguments won't work because the pow method only takes in positional arguments

"""NOTE (3) NOTE"""
# the problem with this class is that _songs is defined outside of the initializer.
# _songs should be defined inside the initalizer as self._songs.

"""NOTE (4) NOTE"""
import io
import contextlib
import unittest

# class Question4Test(unittest.TestCase):
#     def test_blah(self):
#         with contextlib.redirect_stdout(io.StringIO()) as output:
#             pass # this is where you put whatever function you are testing...
#         self.assertEqual(output.getvalue(), 'blah')

"""NOTE (5) NOTE"""
def should_raise(exception_type):
    return ContextManager(exception_type)

class MyCustomException:
    pass

class ContextManager:
    def __init__(self, exception_typ):
        self._exception_typ = exception_typ
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._exception_typ == exc_type:
            print("Succeeding quietly...")
            return True
        else:
            raise MyCustomException


with should_raise(IndexError):
    x = [1, 2, 3]
    x[0]

    




