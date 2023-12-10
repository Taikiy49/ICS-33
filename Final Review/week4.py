"""NOTE Comprehensions NOTE"""
# try some comprehensions...
[x for x in range(5) if x < 3]
[x * x for x in range(5)]
[x.upper() for x in 'Boo']
[x - 1 for x in range(10) if x < 5]

[x * y for x in 'ABC' for y in (1, 2, 3)]
# Now that's pretty cool!

[x * y * z for x in 'ABC' for y in (1, 2, 3) for z in (1, 1, 1) if len(x * y * z) < 3]
# Woh thats long...

[1, 2, 3] == [1, 2, 3]
values1 = [1, 2, 3]
values2 = [[x + 1 for x in range(3)] for _ in range(2)]
values3 = [[1, 2, 3], [1, 2, 3]]

values1 == values2[0]
# BUT values1 is NOT values2[0]
values1 is values2[0]

# IS will only work in certain scenarios
# As long as we use the same value to make a new value, we can use that new value to compare
# with the old value and check both "==" and "is"

other_values1 = [values1] * 4
values1 is other_values1[0]
values1 == other_values1[0]


"""Now lets introduce the __hash__(self) and __eq__(self, other) methods!"""

{x: len(x) for x in ('How', 'is', 'Boo')}
{x: y for x, y in {'Boo': 13, 'Alex': 40}.items()}
{x.upper(): x.lower() for x in ('How', 'is', 'Boo!')}

"""Tuple comprehension is a bit different!"""
(x * x for x in range(5)) # this would print a generator
tuple(x * x for x in range(5)) # this would print an actual tuple
# That's just how it works for tuples

"""Now lets look at them in functions!"""

def f(n):
    return [x for x in range(n)]

# print(f(5))
# print(f(0))

"""Now lets look at the asymptotic analysis"""


# THIS FUNCTION RUNS AT O(1) TIME!!
def elements_at(elements, index):
    return elements[index]

# These next two functions do the same thing, but one of them is more cheaper than the other...
def relatively_cheap(n):
    values = []
    for i in range(n):
        values.append(i)
    return values

def relatively_expensive(n):
    values = []
    for i in reversed(range(n)): # say n is 3, the reversed range will go 2, 1, 0
        values.insert(0, i) # will go in backwards order...
    return values
# insert requires shifting everything inside the list, therefore it costs more.
# especially when the list becomes bigger, it comes more...

# print(relatively_cheap(5))
# print(relatively_expensive(5))

"""NOTE Iteration NOTE"""
(list('Boo'))
([x.upper() for x in 'Boo'])

# Can it even create me a cartesian product?
([(x, y) for x in range(3) for y in range(3)])

# Now lets look at the iter() method! Lets say...
values = [1, 2, 3]
# obviously the list above is iterable...

# use the next method to find the next value in the list...
def iterable_test():
    values = [1, 2, 3]
    i = iter(values)
    print(type(i))
    print(next(i))
    print(next(i))
    print(next(i))


# notice that if you use the del method to delete something from a list,
# the next method simply just skips the index as it should very nicely. 

def iterable_test_with_del():
    values = [3, 6, 9, 12, 15]
    i = iter(values)
    print(next(i))
    print(next(i))
    del values[3]
    print(next(i))
    print(next(i))
    # ouput: 3, 6, 9, 15

"""So what is considered __iter__?"""
def what_is_considered_iter():
    print(type([1, 2, 3].__iter__()))
    print(type('some_string'.__iter__()))
    print(type(range(5).__iter__()))
    # output: list_iter, string_iter, range_iter <- all of these are classes!

"""Now that we know what iter() and next() do, lets introduce __iter__ and __next__"""
def introducing_more():
    values = [5, 10, 15, 20, 25]
    i = iter(values)
    for _ in range(len(values) + 1):
        try:
            print(i.__next__())
        except StopIteration:
            print("Index is out of the range!")

def more_ranges():
    try:
        print([x for x in range(3, 7)])
        print([x for x in range(0, 10, 2)])
        print([x for x in range(start=0, stop=10, step=2)]) # this is actually illegal because ranges
                                                            # don't take keyword arguments...
    except TypeError as e:
        print(e)

class MyRange:
    def __init__(self, start, stop=None, step=None, /): # <- remember, / means positional only...
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
        self._start = start
        self._stop = stop
        self._step = step
    
    def __repr__(self): # This is called a representation. This method is used if you don't
                        # want to see <class blah blah>
        return f'MyRange({self._start}, {self._stop}, {self._step})'


def run_myrange():
    myrange = MyRange(5, 10, 2)
    print(myrange)

"""Before we continue working on our range, let's do something that uses the repr method again..."""

class TestRepr:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __repr__(self):
        return f'TestRepr({self._name}, {self._age})'

class TestWithoutRepr:
    def __init__(self, name, age):
        self._name = name
        self._age = age

def run_test_reprs():
    print(TestRepr('taiki', 19))
    print(TestWithoutRepr('taiki', 19))

"""Ok lets get back to talking about the range class now!"""

class MyRange2:
    def __init__(self, start, stop=None, step=None, /):
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
        
        self.check_if_int(start, stop, step)
    
        self._start = start
        self._stop = stop
        self._step = step


    """You don't really need these next lines of code..."""

    # def start(self):
    #     return self._start
    
    # def stop(self):
    #     return self._stop

    # def step(self):
    #     return self._step

    # def __str__(self): # the str method is usually a more user-friendly way compared to...
    #     return "This is the string representation!"


    def __repr__(self): # the repr method where it is more usually used for debugging purposes.
        return f'MyRange2({self._start}, {self._stop}, {self._step})'
 
    def __iter__(self): # this is very interesting. we are basically giving all of our attributes
                        # to this new class, which is the range iterator class
        return MyRange2Iterator(self)

    @staticmethod
    def check_if_int(x, y, z):
        if type(x) is int and type(y) is int and type(z) is int:
            pass
        else:
            raise TypeError("Only integer inputs...")

"""It's already pretty complicated, but wait... it gets more complicated when we build the iterator!"""

class MyRange2Iterator:
    def __init__(self, myrange_class):
        self._myrange_class = myrange_class
        self._next = myrange_class._start
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self._myrange_class._stop:
            raise StopIteration
        else:
            result = self._next
            self._next += self._myrange_class._step
            return result

def test_next_works():
    r = MyRange2(6)    
    i = iter(r)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    # At this point, you realize that it doesn't stop...

def test_list_format_works():
    print(list(MyRange2(0, 10, 2)))
    # NOW THAT'S COOL!

# But then again... There is so much more we have to implement to my range class...
# But that's what we have the builtin range for XD

"""NOTE Generators NOTE"""
# the YIELD statement!
# say we have something like this...

def int_sequence(start, end): 
    current = start
    while current < end:
        yield current # what exactly does this even do?
        current += 1

def run_int_sequence():
    print(int_sequence(1, 10))
    # output: <generator blah>
    # I think I see where this is going...

def run_int_sequence_again():
    r = int_sequence(5, 10)
    i = iter(r)
    for _ in range(3):
        print(next(i))
    # output: 5, 6, 7
    # AHHH I SEE SO IT BASICALLY STORES EVERYTHING
    # because if it is returned, it will stop at 5. We won't have any information after it reaches the 
    # first number 5, which is not what we want. We want to know everything that happens after 5 till the end!


"""What if we yield integers? And what if we have return inside generators?"""
def return_in_generator():
    yield 1 
    return 3
    yield 5

def test_return_in_generator():
    i = return_in_generator() # <- this is unnecessary because generators are already 
                            # basically have iter() implemented
    print(next(i))
    print(next(i)) 
    # output: 1, StopIteration

# a return stops the iteration once it is reached...

# What if we raise an exception inside?
def generator_with_exception():
    yield 1
    yield 2
    raise ValueError('Hello')
    yield 3

# output: 1, 2, ValueError

"""Lets create that int sequence again and make it iterable!"""

class IntSequence:
    def __init__(self, start, end):
        self._start = start
        self._end = end
        self._current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= self._end:
            raise StopIteration
        else:
            result = self._current
            self._current += 1
            return result

def run_int_sequence_class():
    int_sequence = IntSequence(1, 10)
    i = iter(int_sequence)
    for _ in range(5):
        print(next(i))

# Lets use generators for files!
def read_lines_from_file(file_path):
    with open(file_path, 'r') as in_file:
        for line in in_file:
            yield line

i = read_lines_from_file('../ICS-33/Final Review/taiki.txt')
# now we have a generator with each line of the file. we can use next() to access the next line.

"""we can do something cool like this..."""
def read_all_integers():
    while True:
        inp = input("Please enter a digit: ")
        if not inp.isdigit():
            break
        yield int(inp)
 
# values = list(read_all_integers())
# input: 1, 2, 3 | output: [1, 2, 3] NOW that's pretty useful!

# this would print out every input as long as they are digits!
for value in read_all_integers():
    print(value)

