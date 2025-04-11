chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types)

for chai in chai_types:
    print(chai, ":", chai_types[chai])

for key, value in chai_types.items():
    print(key, ":", value)

print(chai_types.get("Masala")) # Spicy 
print(chai_types.get("Masalaaaa")) # None 
print(chai_types.get("Masalaaaa", "Not Found")) # Not Found
print(chai_types["Masala"]) # Spicy
# print(chai_types["Masalaaa"]) # KeyError

chai_types["Earl Grey"] = "Citrus" # Adding a new key-value pair
print(chai_types)

squared_nums = {x: x**2 for x in range(5)}
print(squared_nums) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

squared_nums.clear() # Clearing the dictionary
print(squared_nums)

keys = ["Masala", "Ginger", "Green"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict) # {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Green': 'Delicious'}

new_dict = dict.fromkeys(keys, keys)
print(new_dict) # {'Masala': ['Masala', 'Ginger', 'Green'], 'Ginger': ['Masala', 'Ginger', 'Green'], 'Green': ['Masala', 'Ginger', 'Green']}