"""NOTE Asymptotic Analysis NOTE"""
# JUST STUDY THIS ON PEN AND PAPER...
# TOO HARD TO TYPE LOL

"""NOTE Searching NOTE"""
# Sequential searching!

def sequential_search(items: list, key: object) -> int | None:
    for i in range(len(items)):
        if items[i] == key:
            return i
    return None
"""that's how you do sequential searching, but it takes too much time and memory.
    huh... what's another way of doing the same thing with less time and memory then??"""

# Binary searching!

def binary_search(items: list, key: object) -> int | None:
    first = 0
    last = len(items) - 1

    while first <= last:
        middle = (first + last) // 2
    
        if items[middle] == key:
            return middle
        elif items[middle] > key:
            last = middle - 1
        else:
            first = middle + 1
    return None

"""So in a binary search, we first start by setting variables equal to each ends of the list.
    The first end being the first index, and the last end being the length of the list subtracted by 1.
    Now that we have both ends of the list, we want to split the entire list into two, and find the 
    index of that center. We will then use the center index to see if the value is greater or less than the key.
    Or equal of course! Whatever we get, we pick one side of the list, and keep the while list to continue running
    until it breaks the while loop where the first index is somehow less than the last index, or if the first index
    is equal to the last index.
    
    Why wouldn't we always want to use binary search then? You wouldn't want to use binary search all the time
    because code can get more complex where you might need to add and remove elements from the list.
    Then definitely binary search would not work or be very ineffecient. 
"""

