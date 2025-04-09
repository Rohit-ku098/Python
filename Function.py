
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