# and, or, not


x = -1
if x == 1 or x == -1:
    print("x is =", x)
    print(x)
if x > 0:
    print("x is positive")
else:
    print("x is negative")
print("finish")

# only one is executed using elif
name = "Max"
# name = input("Enter a Name: ")
if name == "Max":
    print("Name Entered is :", name)
elif name == "Leo":
    print("Name Entered is :", name)
elif name == "Lily":
    print("Name Entered is :", name)
else:
    print("The Name is not in our data base")

x = 10
if x < 0:
    print("x is positive")
else:
    print("x is negative")
    if (x % 2) == 0:
        print("x is even")
    else:
        print("x is odd")

a = 33
b = 200
if b > a:
    pass
# pass is like continue for if statement

print("while loop")
i = 0
while i < 6:
    i += 1
    if i == 3:
        print("skip 3")
        continue
    print(i)

print()

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

for x in range(6):
    print(x)
# exclusive 6

for x in range(4, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)
else:
    print("Finally finished!")

adj = [1, 2, 3]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
