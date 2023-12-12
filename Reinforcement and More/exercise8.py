"""NOTE (1) NOTE"""
# make me a decorator called class_method that when used on a function defined within a class,
# it converts it into a class method, meaning two things...
# 1) method can be called on the class as a whole, rather than on an object of that class.
# 2) whether called on the class as a whole or an object of that class, its first parameter will be the
#    class rather than an object of that class. in other words, rather than havng a self parameter, it has
#    a cls parameter...
class ClassMethodDescriptor:
    def __init__(self, func):
        self._func = func
    def __set_name__(self, cls, name):
        self._cls = cls
    def execute(self, *args, **kwargs):
        return self._func(self._cls, *args, **kwargs)
    def __get__(self, obj, objtype): # get is used here to grab the arguments in the class Thing
                                     # it's arguments are the object and the type of the object...
        return self.execute

def class_method(func): # <- decorator function!
    return ClassMethodDescriptor(func)

class Thing:
    @class_method
    def foo(cls, x, y):
        return (cls.__name__, x + y)

"""Let's try and create the class method again!"""
class ClassMethodDescriptor:
    def __init__(self, func):
        self._func = func
    def __set_name__(self, cls, name):
        self._cls = cls
    def __get__(self, obj, objtype):
        return self.execute
    def execute(self, *args, **kwargs):
        return self._func(self._cls, *args, **kwargs)

def class_method(func):
    return ClassMethodDescriptor(func)


"""NOTE (2) NOTE"""
# remember, __getattr__ is called only if looking up an attribute in a dictionary fails
# remember, __setattr__ and __delattr__ is called regarless of whether the attribute is present in the object's dictionary.

# why __getattr__ is called only if lookng up an attribute in a dictionary fails is because most of the time,
# there's no need to have __getattr__ when looking up an attribute in a dictionary is succeesful because
# __setattr__ and __delattr__ will have successfully modified the attribute or deleted the attribute it needed to.
# though if __setattr__ didn't have an attribute to set or if __delattr__ didn't have an attribute to delete,
# __getattr__ is called to tell you that the looking up an attribute in a dictionary failed...

# SOMETHING NEW I LEARNED...
"""another reason why I believe the __getattr__ method is only called when looking up an attribute in 
   a dictionary fails is because it will become complicated if we try to either overwrite an attribute that
   already exists by using the __getattr__ method. That's why the __setattr__ method is there to do that...
"""

"""NOTE (3) NOTE"""
# write a class named LimitedString meeting the following requirements...
# LimitedString is a descriptor, length is no longer the maximum length...
# implement can_delete which controls whether an attribute described by it can be deleted from an object.
# True if can, False if cannot...

class LimitedString:
    def __init__(self, max_length, *, can_delete=True):
        self._max_length = max_length
        self._can_delete = can_delete
    def __set_name__(self, cls, name):
        self._attribute_name = name
   
    def __get__(self, obj, objtype):
        if obj is not None:
            return getattr(obj, self._attribute_name)
        else:
            return self
    def __set__(self, obj, value):
        if obj is None:
            return
        elif type(value) is not str:
            raise ValueError("Not a string")
        elif len(value) > self._max_length:
            raise ValueError("Length exceeds length limit")
        else:
            setattr(obj, self._attribute_name, value)

    def __delete__(self, obj):
        if obj is None:
            return
        elif self._can_delete:
            delattr(obj, self._attribute_name)
        else:
            raise AttributeError("Atrribute cannot be deleted...")



class Thing:
    name = LimitedString(10)

t = Thing()
t.name = 'Boo'
print(t.name)
t.name = 'Boo is perfect this afternoon'
print(t.name)
