import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


@timer
def example_function(n):
    time.sleep(n)
    return n

example_function(2)



# Q2. Write a decorator that prints the arguments and return value of a function.

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"FunctionName: {func.__name__} Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Rohit", greeting="Hello")


## Q3. Cacheing Decorator

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def example_fun(n):
    time.sleep(n)
    return n



print(example_fun(2))
print(example_fun(2))
print(example_fun(4))



