"""NOTE (1) NOTE"""
# What is the job title held by Renate Mayer
""" 
SELECT title
FROM employee
WHERE name = "Renate Mayer";
"""

# What are the names of the employees in the department named Executive Management
""" 
SELECT e.name
FROM employee as e 
    INNER JOIN membership AS m ON m.employee_id = e.employee_id
    INNER JOIN department AS d ON d.department_id = m.department_id
WHERE d.name = "Executive Management";
"""

# What are the names of the employees who report to Andraste Lemoine
"""
SELECT e.names
FROM employee as e
    INNER JOIN employee_manager AS em ON em.employee_id = e.employee_id
    INNER JOIN employee AS m on m.employee_id = em.manager_id
WHERE m.name = "Andraste Lemoine";
"""

"""NOTE (2) NOTE"""
def multiples(count, multiplier):
    return [multiplier * (i + 1) for i in range(count)]

def with_non_zero_lengths(*args):
    return {value: len(value) for value in args}

def make_diagonal(n):
    return [['B' if k == i else None for k in range(n)] for i in range(3)]


"""NOTE (3) NOTE"""
# I believe that the keys in a dictionary should be hashable so we are able to access it's values easily by
# calling its key. If both the key and value are hashalbe, then I believe it would cause a problem... The values
# in a dictionary do not have to be unique, meaning it could be possible to have duplicate values.

# in terms of time complexity, in a dictionary with millions of keys in it, we want to beable to figure out what
# the value associated with the key 'Boo' is in O(1) time...

"""NOTE (4) NOTE"""
# dictionary comprehension to construct a dictionary containing n keys and their associated values would take
# checking whether a key exists takes O(1) time because its hash will determine where it is...
# adding a new key also takes O(1) time for the same reason.
# With a total number of n key/value pairs to be added, this would resonably be expected to take a total of
# O(n) time because O(1) + O(n) = O(n)