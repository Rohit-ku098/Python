x = 2
y = 3 
z = 4

print(x + y + z)

a, b = x+2, y+3

print(a, b)

pow = x**2
print(pow)

# comparison
print(1 < 2) # True
print(1 > 2) # False
print(1 == 2) # False
print(1 != 2) # True

print(1 < 2 < 3) # True
print(1 < 2 and 2 < 3) # True

print(1 == 2 < 3) # False
print(1 == 2 and 2 < 3) # False

import math
print(math.floor(4.4)) # 4
print(math.ceil(4.4)) # 5

print(math.floor(-4.4)) # -5
print(math.ceil(-4.4)) # -4

# trunc - Removes the decimal part
print(math.trunc(4.4)) # 4
print(math.trunc(-4.4)) # -4

## complex number
a = 2 + 3j
b = 4 + 5j

print(a + b) # (6+8j)

## Octal number
a = 0o123 # 83
print(a)

## Hexadecimal number
a = 0xFF # 255
print(a)

## Binary number
a = 0b101 # 5
print(a)


import random

rand = random.random() # Generates a random number between 0 and 1
print(rand)

print(random.randint(1, 10)) # Generates a random number between 1 and 10


## Decimal
print(0.1 + 0.1 + 0.1) # 0.30000000000000004
print(0.1 + 0.1 + 0.1 - 0.3) # 5.551115123125783e-17

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # 0.0


## Infinity
infinity = float('inf')
print(infinity)

## Set
setone = {1,2,3,4}
print(setone & {1,5}) # intersection - {1}
print(setone | {1,5}) # union - {1,2,3,4,5}
print(setone - {1,5}) # difference - {2,3,4}

