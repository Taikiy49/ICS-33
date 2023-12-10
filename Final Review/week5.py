"""NOTE Using and Combining Generators NOTE"""
# generator comprehensions return generators, just like generator functions do!
gen_comp = (x for x in range(5)) # remember this is an example of a generator comprehension. yes tuple comprehension!
# tuple comprehensions give me a generator. <generator blah blah>

i = (x * x for x in range(100000000))
# for _ in range(10):
#     print(next(i))

"""we can also build generators that gives me multiple results at time..."""

def take_three_return(values):
    i = iter(values)
    return [next(i), next(i), next(i)]
# you can also write it like this
def take_three_yield(values):
    i = iter(values)
    for _ in range(3):
        yield next(i)
# print(list(take_three_yield([x * x for x in range(10)]))) very interesting!

# we can also ask for how many you want to yield...
def take_count(count):
    values = [x * x for x in range(100)]
    i = iter(values)
    for _ in range(count):
        try:
            yield next(i)
        except StopIteration: # this is how we would peacefully handle a situation where the count is
                              # greater than the amount yielded.
            break

# print(list(take_count(10)))

"""Now lets look at another situation..."""
def concatenate(first, second):
    result = []
    for value in first:
        result.append(value)
    for value in second:
        result.append(value)
    return result
# now... can we do the same thing with yield?
def concatenate(first, second):
    for value in first:
        yield value
    for value in second:
        yield value
# nice! this works... but is there a more simpler way??
def concatenate(first, second):
    yield from first
    yield from second
# YUP! THIS WORKS! WAIT BUT THERE'S MORE...
def concatenate(*sequences):
    for sequence in sequences:
        yield from sequence

# print(list(concatenate(take_count(5), take_count(10), take_count(100)))) # now it can literally take in as many
#                                                                          # sequences as it wants :)
#                                                                          # NOW THAT'S AWESOME!

"""introducing more builtin functions in Python!"""
# LAMBDA
# FILTER
# ANY
# ALL
# ENUMERATE
# ZIP

x = list(map(lambda n: n * n, [1, 2, 3]))
# map applies a function to each element in an iterable
y = list(filter(lambda n: n > 0, [-1, -3, 1, 5, -7]))
# returns only truthy values...
z = any(['Boo', 'is', 0])
# returns True if any of the values in the iterable are True...
m = any(len(n) > 3 for n in ['Boo', 'is', 'happy'])
n = all(['Boo', 'is', 'happy', 0])
# ONLY returns True if all the values in the iterable are True...

z = list(enumerate(['Boo', 'Taiki']))
# output: [(0, 'Boo'), (1, 'Taiki')]
x = list(zip(['Boo', 'Taiki', 'Mari'], ['age', 'weight', 'level'], [13, 150, 10]))
# zip can combine more than two iterables... 
# output: [('Boo', 'age', 13), ('Taiki', 'weight', 150), ('Mari', 'level', 10)]

"""Introducing itertools!"""
import itertools
# itertools.isslice()
# itertools.count()
# itertools.repeat()
# itertools.chain()

a = list(itertools.islice('Boo is happy today', 6))
# output: ['B', 'o', 'o', ' ', 'i', 's']
b = list(itertools.islice('Boo is happy today', 5, 10))
# output: ['s', ' ', 'h', 'a', 'p'] WOW you can even give it a range to slice...
c = list(itertools.islice(itertools.count(8), 10))
# output: [8, 9, 10, 11, 12, 13, 14, 15, 16, 17] # start from count basically?
d = list(itertools.islice(itertools.chain('Boo', 'Taiki'), 7))
# output: ['B', 'o', 'o', 'T', 'a', 'i', 'k'] # You can even put two strings together!

"""NOTE Python Data Model NOTE"""
# INTRODUCING __len__

class MyRange:
    def __len__(self): # to write our len dunder method, we could just use len() or sum(), but they are both
                       # too expensive. it also defeats the whole purpose of writing this __len__ method...
        count = 0 
        for value in self:
            count += 1
        return count
# what we did above will take O(n) time because we're still iterating the values in the ratnge from beginning to end.
# so how else can we write our __len__ method?

class MyRange:
    def __len__(self):
        return max(0, math.ceil((self._stop - self._start) / self._step))
# THIS WILL TAKE O(1) TIME...
# what we do is basically compare which number is bigger, 0, meaning the length is 0, or...
# where the stop is, subtracted by the start to get the sub indexes. then we divide it by the step, just in case
# sub indexes are supposed to be taken in steps of more than 1.

# INTRODUCING __bool__
class Person:
    def __init__(self, name=''):
        self._name = name
    def __bool__(self): # you return what you want to make truthy. basically...
        return self._name != ''

(bool(Person())) # in this case, this will return False because the name is empty
(bool(Person('Taiki'))) # in this case, this will return True because the name is non-empty...

# INTRODUCING __getitem__
class MyRange:
    def __getitem__(self, index): # it takes the index as an argumnet...
        if type(index) is not int:
            raise TypeError("Index must be an integer.")
        elif index < 0 or index >= len(self):
            raise IndexError("Index out of range.")
        
        return self._start + index * self._step
# very complicated but interesting...

# lets give it another example!
class ThreeSequence:
    def __len__(self):
        return 3
    def __getitem__(self, index):
        if 0 <= index < len(self):
            return index * 3
        else:
            raise IndexError("Index out of range")
        
s = ThreeSequence()
# (s[0], s[1], s[2], s[3]) # since the __len__ is 3, index to the 3 will result in an IndexError

([i for i in s]) # [0, 3, 6]
([i for i in range(10)]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
([i in s for i in range(10)]) # [True, False, False, True, False, False, True, False, False, False]

"""Introducing the slice builtin..."""
s = slice(1, 10, 2)
(s.start, s.stop, s.step)

# implementing slice into __getitem__...
class MyRange:
    def __getitem__(self, index):
        if type(index) is int:
            if 0 <= index < len(self):
                return self._start + index * self._step
            else:
                raise IndexError("Index is out of range...")
        elif type(index) is slice:
            start, stop, step = index.indices(len(self))
            start_value = self._start + start * self._step
            stop_value = min(self._start + stop * self._step, self._stop)
            step_value = step * self._step
        else:
            raise TypeError("Not an index or slice...")


"""INTRODUCING __hash__"""
(hash('Boo'))
(hash('Boo'))
# these two strings have the same hash...

# (hash([1, 2, 3])) # mutable objects cannot be hashed.

class MyRange:
    def __hash__(self):
        return hash((self._start, self._stop, self._step))
# that's what you would implement to your MyRange class for it to be comparable.

# Let's use implement the hash method in another class!
class Hashable:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __hash__(self):
        return hash((self._name, self._age))

a = Hashable('taiki', 19)
b = Hashable('mari', 18)
c = Hashable('taiki', 19)

(hash(a)==hash(c)) # output: True
(hash(a)==hash(b)) # output: False
# nice!
"""Now lets look an example where the class is not hashable..."""
class NotHashable:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
a = NotHashable('taiki', 19)
b = NotHashable('mari', 18)
c = NotHashable('taiki', 19)

# in this case, even though a and c have the same arguments, they will both have different hash numbers...
# this is why we need to implement __hash__ to assign them their respective hash numbers. 

"""Indentity and equivalence"""
# remember...
[1, 2] < [1, 2, 3]
# output: True

"""INTRODUCING __eq__"""
# now these dunder methods are really cool!
# say we have...

class MyRange:
    def __eq__(self, other):
        if type(other) is MyRange:
            return self._start == other._start and self._stop == other._stop and self._step == other._step
        else:
            return NotImplemented
# this way, the eq method will check if these two classes are equivalent

"""Lets take a look at another class with a __eq__ dunder method..."""

class ImplementedEq:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __eq__(self, other):
        if type(other) is ImplementedEq:
            return self._name == other._name and self._age == other._age
        else:
            return NotImplemented

a = ImplementedEq('taiki', 19)
b = ImplementedEq('mari', 18)
c = ImplementedEq('taiki', 19)

(a == b, a == c, c == b) # output: False, True, False)
# awesome! now we can see if classes share same attributes!!

"""NOW lets introduce __lt__ and __le__"""
class EverythingImplemented:
    def __init__(self, value):
        self._value = value
    def __eq__(self, other):
        if type(other) is EverythingImplemented:
            return self._value == other._value
        else:
            return NotImplemented
    def __lt__(self, other):
        return self._value < other._value
    def __le__(self, other):
        return self._value <= other._value

a = EverythingImplemented(13)
b = EverythingImplemented(15)
c = EverythingImplemented(13)

(a < b) # output: True
(a > b) # output: False
(a == b) # output: False
(a <= b) # output: True
(a >= b) # output: False

# Now let's add more to our class...
"""INTRODUCING __add__, __sub__, __mul__, __truediv__, __floordiv__, __pow__"""
"""You can also add r in front of them to flip the method: __radd__, r__mul__, etc."""
"""You can also add i in front of them to add i to the object in place: __iadd__, __isub__, etc."""
"""The __iadd__ and __isub__ and anll those other i methods are used for +=, -=, etc."""

class EverythingImplemented:
    def __init__(self, value):
        self._value = value
    def __eq__(self, other):
        if type(other) is EverythingImplemented:
            return self._value == other._value
        else:
            return NotImplemented
    def __lt__(self, other):
        return self._value < other._value
    def __le__(self, other):
        return self._value <= other._value
    def __add__(self, other):
        if type(other) is EverythingImplemented:
            return EverythingImplemented(self._value + other._value)
        elif type(other) is int:
            return EverythingImplemented(self._value + other)
    def __rsub__(self, other):
        if type(other) is EverythingImplemented:
            return EverythingImplemented(self._value - other._value)
    def __floordiv__(self, other):
        if type(other) is EverythingImplemented:
            return EverythingImplemented(self._value // other._value)
    

a = EverythingImplemented(5)
b = EverythingImplemented(6)
c = EverythingImplemented(5)

a = a + b
print(a._value)
a += 3
print(a._value)

