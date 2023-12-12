"""NOTE Abstract Base Class NOTE"""
import collections.abc
days = 365

class Person(collections.abc.Sized):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    def __len__(self):
        return self._age * days

p = Person('Boo', 13)
(len(p)) # output: 4745

"""
The immediate benefit of collections.abc.Sized is that it knows the basic requirement that the
__len__ method is necessary.
"""
# for example, take a look at this...
class NotReallySized(collections.abc.Sized):
    pass

# n = NotReallySized() # output: ERROR because there is not __len__ method!

# this can be very useful in situations like this...
class Sized: 
    def __init__(self, value, size):
        self._value = value
        self._size = size
    def __len__(self):
        return self._size
    # def __getattr__(self, name):
    #     return name
    # def __setattr__(self, name, value):
    #     super().__setattr__(name, value)
    # def __delattr__(self, name):
    #     super().__delattr__(name)

s = Sized(5, 10)
(isinstance(s, collections.abc.Sized)) # output: True!
(hasattr(s, '_value'))
(hasattr(s, 'does_not_exist'))


from collections import abc

"""Now lets use the abstract base class decorator!"""
class HasName(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplementedError
    
class Person(HasName):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

p = Person('Boo')
print(isinstance(p, HasName))
