"""NOTE (1) NOTE"""
def all_substrings(string):
    return IteratorClass(string)

class IteratorClass:
    def __init__(self, string):
        self._string = string
        self._start = 0
        self._length = 1

    def __iter__(self):
        return self
    def __next__(self):
        if self._start + self._length < len(self._string):
            self._start = 0
            self._length += 1

        if self._length > len(self._string):
            raise StopIteration
        
        next_substring = self._string[self._start : (self._start + self._length)]
        self._start += 1
        return next_substring

i = (all_substrings('123'))

"""NOTE (2) NOTE"""
# remember, generators have a yield statement!
def generate_range(start, stop=None, step=None, /):
    if stop is None:
        stop = start
        start = 0
        step = 1
    elif step is None:
        step = 1

        
    while start <= stop - 1:
        yield start 
        start += step
    
def no_fizz_without_buzz(n):
    for z in range(30):
        if n % 3 == 0 and n % 5 == 0:
            yield n
        n += 1

"""This cartesian product question is way too hard..."""

"""NOTE (3) NOTE"""
def no_fizz_without_buzz(n):
    for z in range(30):
        if n % 3 == 0 and n % 5 == 0:
            yield n
        n += 1

class NoFizzWithoutBuzz:
    def __init__(self, n):
        self._n = n 
    def __iter__(self):
        return self
    def __next__(self):
        if self._n % 3 == 0 and self._n % 5 == 0:
            return self._n
        self._n += 1


"""NOTE (4) NOTE"""
# the problem with iterators is that once we go forward, we can't go back. That's why there's an issue if we
# try to index something after we already indexed something further ahead. It's just how iterators work, 
# and this way it keeps it simple. 




