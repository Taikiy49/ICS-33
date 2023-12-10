"""NOTE Inheritance NOTE"""
# this is how we use inheritance for classes...
class Base:
    def first(self):
        return 13
class Derived(Base):
    def second(self):
        return 17

def test_derived():
    d = Derived()
    print(d.second()) # output: 17
    print(d.first()) # output: 13

    print(isinstance(d, Derived)) # True
    print(isinstance(d, Base)) # True
    # It's safe to treat d as Derived and Base!

# What if we have a base and a derived class that have the same method names?
class Base:
    def value(self):
        return 13
class Derived(Base):
    def value(self): 
        base_value = super().value() # we can use super() to access the value from the base class instead!
                                     # how useful super can be in cases like these!
        return 20 * base_value

def test_derived():
    print(Derived().value())
    print(Base().value())

"""You can use inheritance for errors as well, same way you kind of used it in one of the projects..."""
class CustomValueError(ValueError):
    pass
def error():
    try:
        raise CustomValueError
    except ValueError:
        print("A normal ValueError was caught")
    except CustomValueError:
        print("My special ValueError was caught!")
# in this case, since the base class is a value error and the derived class is my custom value error,
# when we raise my CustomValueError, it will catch the normal ValueError in the exception first.
# this is because exceptions go in order!

"""Have some fun! Make a pokemon with 2 different evolutions using a base class with two derived classes!"""
class Eevee:
    def level(self):
        return 20

class Vaporeon(Eevee):
    def info(self):
        level = super().level() + 5
        return level, 'blue'

class Jolteon(Eevee):
    def info(self):
        level = super().level() + 10
        return level, 'yellow'

def test_pokemon():
    print(Eevee().level())
    print(Vaporeon().info())
    print(Jolteon().info())
    # fun stuff!


