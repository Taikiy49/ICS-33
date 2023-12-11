"""NOTE (1) NOTE"""
class MultipleSequence:
    def __init__(self, length, sequence_multiplier=1, /):
        self._length = length
        self._sequence_multiplier = sequence_multiplier

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if 0 < index < self._length:
            return self._sequence_multiplier * index
        else:
            raise IndexError("Index is not in range...")

    def __contains__(self, value):
        return int(value) % self._multiplier == 0
    
    def __bool__(self):
        return self._length > 0

    def __iter__(self):
        return self

    def __repr__(self):
        return f'MultipleSequence({self._length}, {self._sequence_multiplier})'
        

"""NOTE (2) NOTE"""
class Collection:
    def __init__(self, values):
        self._values = values
    def __eq__(self, other):
        if type(other) is not Collection:
            raise TypeError("Comparing with non Collection object!")
        if self._values == other._values:
            return True
        else:
            return False
    def __lt__(self, other):
        if self._values < other._values:
            return True
        else:
            return False
    def __le__(self, other):
        if self._values < other._values:
            return True
        else:
            return False

a = Collection(5)
b = Collection(7)

"""NOTE (3) NOTE"""
class Wailmer:
    def __init__(self, pokemon_type, pokemon_level):
        self._pokemon_type = pokemon_type
        self._pokemon_level = pokemon_level
    def pokemon_type(self):
        return self._pokemon_type
    def pokemon_level(self):
        return self._pokemon_level
    def __eq__(self, other):
        if type(self) is Wailmer:
            return self._pokemon_type == other._pokemon_type and self._pokemon_level == other._pokemon_level


class Wailord(Wailmer):
    def __init__(self, pokemon_size):
        self._pokemon_size = pokemon_size
    def pokemon_size(self):
        return self._pokemon_size
    def pokemon_info(self):
        return f'Type: {super().pokemon_type()}, Level: {super().pokemon_level()}, Size: {self.pokemon_size()}'
    def __eq__(self, other):
        if type(self) is Wailord:
            return self._pokemon_size == other._pokemon_size


class WailQueen(Wailmer):
    def __init__(self, pokemon_size):
        self._pokemon_size = pokemon_size
    def pokemon_size(self):
        return self._pokemon_size
    def pokemon_info(self):
        return f'This pokemon is {self.pokemon_size()} pounds!'
    def __eq__(self, other):
        if type(self) is Wailord:
            return self._pokemon_size == other._pokemon_size

"""NOTE (4) NOTE"""
a = {1, 2, 3}
b = {4, 5, 6}
c = a | b 

#Intoruding __or__, __ror__, __ior__ methods... because I couldn't find them anywhere in my notes :)

class Or:
    def __init__(self, age):
        self._age = age
    def __or__(self, other):
        return self._age | other._age
class Ror:
    def __init__(self, age):
        self._age = age
    def __ror__(self, other):
        return self._age | other._age
class Ior:
    def __init__(self, age):
        self._age = age
    def __ior__(self, other):
        self._age |= other._age
        return self

"""
Summary:
__or__ is for the left side of '|'
__ror__ is for the right side of '|' when the left side doesn't support it
__ior__ is for the in-place modification
"""

# the ror method would not be necessary. Since the | operator can only be used to combine
# a set or another set or a dictionary wth another dictionary. Therefore, there's no scenario where
# the reflected version of | would be needed. 

# the ior method would be a necessity because its just simpler. instead of copyng both sets or dictionaries, 
# it could add keys into an existing set or dictionary, so that only the right collection would have to be
# copied into the left one.





    






    

