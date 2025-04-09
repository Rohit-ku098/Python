tea_varities = ["Black", "Green", "Oolong", "White"]

print(tea_varities)

## Slicing
print(tea_varities[0:2]) # ['Black', 'Green']
print(tea_varities[:3]) # ['Black', 'Green', 'Oolong']

tea_varities[3] = "Herbal"
print(tea_varities)

for tea in tea_varities:
    print(tea, end=" ") # Black Green Oolong Herbal
print()

tea_varities.append("Darjeeling")
print(tea_varities) # ['Black', 'Green', 'Oolong', 'Herbal', 'Darjeeling']

tea_varities.pop() # Removes the last element and returns it
print(tea_varities) # ['Black', 'Green', 'Oolong', 'Herbal']

tea_varities.remove("Oolong") # Removes the specified element
print(tea_varities) # ['Black', 'Green', 'Herbal'] 

tea_varities.insert(2, "Masala") # Inserts the element at the specified position
print(tea_varities) # ['Black', 'Green', 'Masala', 'Herbal']


squared_nums = [x**2 for x in range(10)]
print(squared_nums) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

