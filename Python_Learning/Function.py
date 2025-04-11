
def sum(numOne, numTwo):
    return numOne + numTwo

print(sum(3,4))

def circle_stats(radius):
    area = 3.14 * radius**2
    circumference = 2 * 3.14 * radius
    return area, circumference


area, circumference = circle_stats(5)
print(area)
print(circumference)


### lambdas
cube = lambda x: x**3 # lambda parameter: expression
print(cube(3))

def sum_all(*args): # *args allows for an arbitrary number of arguments
    total = 0
    print(type(args)) # args is a tuple
    for num in args:
        total += num
    return total

print(sum_all(1,2,3,4,5)) # 15

def print_fullname(first_name, last_name):
    print(f"Full name: {first_name} {last_name}")

print_fullname(first_name="Rohit", last_name="Kumar") # Full name: Rohit Kumar


### **kwargs allows for an arbitrary number of keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}") # here f is for formatted string

print_kwargs(name="John", age=30, city="New York") # name: John, age: 30, city: New York
print_kwargs(name="John", age=30) # name: John, age: 30
print_kwargs(name="John") # name: John


### yield - used to create a generator function
# A generator function is a special type of function that returns an iterator object
def even_generator(limit):
    for num in range(2, limit+1, 2):
        yield num # yield returns a value and pauses the function, allowing it to be resumed later

# Using the generator function
for num in even_generator(10):
    print(num) # 2, 4, 6, 8, 10