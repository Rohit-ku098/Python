
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")


for i in range(10):
    print(i, end=" ")
print()

for i in range(10, 0, -1):
    print(i, end=" ")
print()

for i in range(0, 10):
    print(2, "x", i+1, "=", 2*(i+1)) 