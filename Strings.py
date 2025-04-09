chai = "Masala Chai"

## Slicing
slice_chai = chai[0:6]
print(slice_chai)

num_str = "0123456789"

print(num_str[3:]) # 3456789
print(num_str[:3]) # 012
print(num_str[0:7:2]) # 0246
print(num_str[0:7:3]) # 036
print(num_str[7:0:-1]) #7654321
print(num_str[::2]) #02468
print(num_str[::-1]) #9876543210

# String Functions
chai = "Masala Chai"
print(len(chai))
print(chai.upper()) # MASALA CHAI
print(chai.lower()) # masala chai
print(chai.title()) # Masala Chai
print("   chai  ".strip()) # chai
print(chai.find("a")) # 1

chai = "Lemon Chai"
print(chai.replace("Chai", "Tea")) # Lemon Tea

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(",")) # ['Lemon', ' Ginger', ' Masala', ' Mint']

chai = "Masala Chai Chai Chai"
print(chai.count("Chai")) # 3

print("Chai" in chai) # True

order = "I ordered {} cups of {} chai"
print(order.format(2, "Masala")) # I ordered 2 cups of Masala chai

chai_variety =[ "Lemon", "Ginger", "Masala", "Mint"]
print(" ".join(chai_variety)) # "Lemon Ginger Masala Mint"


## raw string
print("Hello\nWorld")   # Hello
                        # World         
print(r"Hello\nWorld") # Raw string- Hello\nWorld
print(r"c:\users\rohit") # c:\users\rohit