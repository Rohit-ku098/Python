
### Mutable and Immutable
a = "rohit"
a[0] = "R" # Error: String is immutable

a = [1,2,3]
a[0] = 4 # Success: List is mutable

### Data Types

# Here variable do not have data type, it is a reference
# Type is available for the value present at reference

a = 123 # a points to integer value 123
a = 2.34 # a points to float value 2.34
a = "rohit" # a points to string value "rohit"

### Reference
b = a # Reference Copy - a and b both points to same memory location


### Shallow and Deep Copy
myList = [123, "chai", 3.14]
print(myList)

myList2 = myList # Shallow copy - Reference Copy
myList[0] = 456
print(myList) # [456, 'chai', 3.14]
print(myList2) # [456, 'chai', 3.14]

myList3 = myList.copy() # Deep copy - Value Copy
myList[0] = 789
print(myList) # [789, 'chai', 3.14]
print(myList3) # [456, 'chai', 3.14]


### == and is operators
list1 = [1,2,3]
list2 = list1

print(list1 == list2) # True - Value Comparison
print(list1 is list2) # True - Reference Comparison

list3 = [1,2,3]
print(list1 == list3) # True - Value Comparison
print(list1 is list3) # False - Reference Comparison