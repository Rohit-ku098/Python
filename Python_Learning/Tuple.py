## Tuple vs List
# Tuple is immutable
# List is mutable

myTuple = (1,2,3)
print(myTuple)
print(len(myTuple))

myTuple = 1,2,3
print(myTuple)
print(len(myTuple))

# myTuple[0] = 4 # Error - Tuple is immutable
print(myTuple)
print(len(myTuple))