# Number: 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
# String: 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
# List: [1, [2, 'three'], 4.5], list(range(10))
# Tuple: (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
# Dictionary: {'a': 1, 'b': 2, 'c': 3} or dict(a=1, b=2, c=3)
# Set: set('abc'), {'a', 'b', 'c'} - Unique elements

# File: open('eggs.txt'), open(r'C:\eggs\spam.txt', 'wb')

# Boolean: True, False

# None: None

# Functions, modules, classes

# Advanced: Decorators, Generators, Iterators


# Numbers
print(2+2) # 4
print(2*2.3) # 4.6
print(2**3) # 2 to the power of 3
print(2**1000) # 2 to the power of 1000 - It supports large numbers

import random
rand = random.random() # Generates a random number between 0 and 1
print(rand)

import math
print(math.pi)


# Strings
username = "rohit"
print(len(username)) # Length of the string

print(username[0]) # First character
print(username[-1]) # Last character

print(username[0:2]) # First two characters

# username[3] = "a" # Will throw an error because strings are immutable


# Lists
myList = [123, "chai", 3.14]
print(myList)
print(len(myList))

myList2 = myList # Shallow copy - Reference Copy
myList[0] = 456
print(myList) # [456, 'chai', 3.14]
print(myList2) # [456, 'chai', 3.14]

myList3 = myList.copy() # Deep copy - Value Copy
myList[0] = 789
print(myList) # [789, 'chai', 3.14]
print(myList3) # [456, 'chai', 3.14]

# Dictionary
myDict = {"name": "rohit", "age": 22}
print(myDict)
print(len(myDict))
print(myDict["name"])
# print(myDict["lastname"]) # KeyError

myDict.update({"lastname": "kumar"})
print(myDict)

# Tuples
myTuple = (1,2,3)
print(myTuple)
print(len(myTuple))
