"""NOTE (1) NOTE"""
 # this problem was solved externally...

"""NOTE (2) NOTE"""
# O(n) There are n/2 loop iterations. 
# O(1) memory 
# If the function was written this way, it will run in O(n) time as it is appending to the list, but still

# take O(n) time because we are still looping over the list x, and because appending an element to the end
# of a list can be thought to take constant time. 
# O(n) memory because it builds an entirely separate list from the one that was passed into it, and
# the list contains n elements. 

"""NOTE (3) NOTE"""
# although it categorizes functions so broadly, they are very important as they can give you information to
# choose where you not you want to use a function or if a function will meet the needs. Something that runs
# in O(1) time is substantially more cost efficient than something that runs in O(n) time. 

# you should next determine which code will work out better for you in the long run. Just because a function 
# is more time effecient, it does not mean that you should alwyas prefer to use that function. There are scenarios
# where the more time effecient function will not work with something else you're trying to do. 

"""NOTE (4) NOTE"""
# O(n^2) time because appending to a list costs O(n) time.
# O(n) memory because everytime a new value is appended, the old value is destroyed. 

"""NOTE (5) NOTE"""
def binary_search(items: list, key):
    first = 0
    last = len(items) - 1

    while first <= last:
        middle = (first + last) // 2

        if items[middle] == key:
            return middle
        elif items[middle] > key: # the only thing you have to change to be able to accept
                                  # a list in descending order is here!
            first = middle + 1
        else:
            last = middle - 1
    return None

print(binary_search([7, 5, 3, 2, 1], 5))



        