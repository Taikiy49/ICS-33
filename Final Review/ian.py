
class Hello1:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __len__(self):
        return len(self._name)
    def __bool__(self):
        return self._name == 'Ian'
    def __iter__(self):
        return self
    def __next__(self):
        if self._age >= 18:
            raise StopIteration
        else:
            result = self._age
            self._age += 1
            return result
    def __eq__(self, other):
        if type(other) is Hello1:
            return self._age == other._age
        else:
            return NotImplemented
    def __lt__(self, other):
        return self._age < other._age
    def __le__(self, other):
        return self._age <= other._age
    def __hash__(self):
        return hash(self._age)

h = Hello1('Taiki', 14)
# print(bool(h))
# print(len(h))
# print(next(h))
# print(next(h))
# print(next(h))
          
class Descriptor:
    def __init__(self):
        pass
    def __get__(self, instance, name):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
    def __set_name__(self, owner, name):
        pass

class MyRange:
    def __init__(self, start, stop, step):
        self._start = start
        self._stop = stop
        self._step = step
    def __iter__(self):
        return self
    def next(self):
        result = self._start
        if result < self._stop:
            self._start += self._step
            return result
    def __getitem__(self, index):
        return self._start + index * self._step
        

# dunders needed for sequence
class Sequence:
    def __init__(self, string):
        self._string = string
    def __getitem__(self, index):
        return self._string[index]
    def __len__(self):
        return len(self._string)

s = Sequence('abc')
# print(len(s))
# print(next(s)) # this would not work because the class is not an iterator...
# an iterator class needs a __iter__ and __next__ method!

# a generator method needs a yield

# descriptor == decorator!
class Descriptor:
    def __init__(self, func):
        self._func = func
    def __set_name__(self, cls, name): # DONT GET THIS MIXED UP WITH __getattr__ where it actually returns name!!!
        return cls
    def execute(self, cls, *args, **kwargs):
        return self._func(cls, *args, **kwargs)
    def __get__(self):
        return self.execute
    # you can also add dunder methods set and delete
        
    
# dir() returns the current module's __dict__'s keys in a list, in sorted order.


class AttributeShit:
    def __getattr__(self, name):
        return name
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
    def __delattr__(self, name, value):
        super().__delattr__(name, value)


"""Using @staticmethod and @classmethod"""
class Thing:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def age(self):
        return self._age
    @staticmethod
    def static_age(age):
        return age
    @staticmethod
    def static_return():
        return 'Hi Taiki!'

t = Thing('taiki', 19)

(t.age()) # 19 
(t.static_age(15)) # 15
(t.static_return()) # Hi Taiki!

"""So, basically for static methods, you are not supposed to pass self..."""

class Thing2:
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    def value1(self):
        return self._value1
    @classmethod
    def class_method(cls): # remember, this will give me the name of the class!
        return cls.__name__

t2 = Thing2(10, 15)
(t2.value1())
(t2.class_method()) # Thing2

"""make me something with both keyword and positional argumeents..."""
def keyword(**kwargs):
    for kwarg in kwargs.values():
        yield kwarg

def positional(*args):
    for a in args:
        yield a

num_list = list(positional(1, 2, 3, 4, 3, 2))
new_list = sorted([x * x for x in num_list]) # [1, 4, 4, 9, 9, 16]

def keyword_and_positional(a, b, /, c, *, d):
    return [a, b, c, d]

(keyword_and_positional(1, 2, c=5, d=6)) # CORRECT!


"""Make me a contextmanager and use it!"""

class ContextManager:
    def __init__(self, value):
        self._value = value
    def __enter__(self):
        print('Entering...')
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if type(exc_type) is ValueError:
            print("Exiting violenetly...")

# with ContextManager(15) as manager:
#     print(manager._value)
#     manager._value += 1
#     print(manager._value)


"""sequential search and binary search"""
def sequential_search(items, value):
    for i in range(len(items)):
        if items[i] == value:
            return i

def binary_search(items, value):
    first = 0
    last = len(items) - 1

    while first <= last:
        middle = (first + last) // 2

        if items[middle] == value:
            return middle
        elif items[middle] < value:
            first = middle + 1
        else:
            last = middle - 1
    return None


"""write me a dictionary comprehension..."""
nums = [1, 2, 3]
({x: x * x for x in nums})


"""create me an iterator class"""
class Iterator:
    def __init__(self, value):
        self._value = value
    def __iter__(self):
        return self
    def __next__(self):
        self._value += 1
        if self._value > 17:
            raise StopIteration
        else:
            return self._value

i = Iterator(15)

"""create me a generator function"""
def generator(items):
    for i in items:
        yield i

"""combine an iterator with a generator..."""
def generator():
    num_list = [x for x in range(10)]
    i = iter(num_list)
    for _ in range(11):
        try:
            yield next(i)
        except StopIteration:
            break

(list(generator()))
        
"""now, let's look at the difference between yield and yield from..."""
def without_yield(first, last):
    result = []
    for f in first:
        result.append(f)
    for l in last:
        result.append(l)
    return result

def with_yield(first, last):
    for f in first:
        yield f
    for l in last:
        yield l

def with_yield_from(first, last):
    yield from first
    yield from last

(list(without_yield([1, 2, 3], [4, 5, 6])))
(list(with_yield([1, 2, 3], [4, 5, 6])))
(list(with_yield_from([1, 2, 3], [4, 5, 6])))

