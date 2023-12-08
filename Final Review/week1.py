"""NOTE FUNCTIONS AND THEIR PARAMETERS NOTE"""

#  print('How', 'is', 'Boo', 'today', sep='_')

def subtract(m, n):
    return m - n
"""
print(subtract(10, 3))
print(subtract(10, m=3))
# print(subtract(m=3, 10)) # This is invalid because the keyword argument comes before the positional arguement.
"""

# values = [5, 4]
# print(subtract(*values))
# too_many = [5, 4, 3] # This wouldn't work because there are three positional arguments. 
# # print(subtract(*too_many)) 
# too_few = [3]
# # print(subtract(*too_few))

# does_not_work = {'a': 1, 'b': 4}
# print(subtract(**does_not_work))

""" Python made it so that whatever I did above will not work... BUT"""
"""
works = {'m': 5, 'n': 2}
print(subtract(**works))
does_not_work = {'m', 3}
# print(subtract(**does_not_work, 3)) # AGAIN this won't work as well because the keyword argument unpacking
                                # is happening before the positional argument.


works = {'n': 2}
# print(subtract(5, **does_not_work)) # Of course this will not work either because
#                                     # variable does_not_work has m instead of it having
#                                     # n as a keyword argument. 
print(subtract(5, **works))
"""


"""Default arguments"""
# def ask_input(prompt="Please enter an integer: "):
#     return int(input(prompt))


# value1 = ask_input()
# value2 = ask_input()
# print(subtract(value1, value2))

# def this_should_not_be_allowed(first=None, second):
#     print(first, second)
# """What I have above should not be allowed because the default argument comes before the nondefault argument"""

"""This is what will be allowed"""
def add_together(first, second=None):
    if second:
        return first + second
    return first

    
# print(add_together(5, 3))
# print(add_together(5))

def add_to_list(value, lst=[]):
    lst.append(value)
    return lst

# print(add_to_list([5, 4, 3]))
# print(add_to_list(['Hello', 'World'], ['Print: ']))

def maximum(first, *rest):
    if rest:
        largest = first
    else:
        largest = None
        rest = first
    for value in rest:
        if largest is None or largest < value:
            largest = value
    return largest

# print(maximum(5, 3))
# print(maximum([3, 9, 5, 6]))

"""Positional and keyword parameters"""
# use * to make everything to the right of it keyword arguments only
# use / to make everything to the left of it positional arguments only

def test_keyword(a, b, *, c, d):
    return a, b, c, d

test_keyword(1, 2, c=3, d=5) # remember, for keyword arguments, the name of the variables
                             # must also be the same...

def test_positional(a, b, /, c, d):
    return a, b, c, d

test_positional(1, 2, 3, 4)
test_positional(1, 2, c=3, d=5)

"""Now thing of a way where it would be useful to have both positional and keyword restrictions..."""
def subtract(a, b, c, /, *, d=0): #  NOTE / must go before *...
    return d - (a + b + c)

subtract(1, 2, 3)
subtract(1, 2, 3, d=8)
"""NOW THATS PRETTY COOL!"""

# try make something else again! Try implement everything you've learned in week 1!!
def everything(a, b, /, *, c, **kwargs): 
    for i in range(b-a):
        for key, value in kwargs.items():
            print(key, value)
    print(c)

everything(1, 2, a=3, b=5, c=6, this='is cool')

"""NOTE CONTEXT MANAGERS NOTE"""



