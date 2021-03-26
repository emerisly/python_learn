import random

if 5<2:
    print("five > two")
    print("second line")
print("not included")

if 5>2:
    print("ok")

# print("OK")
# line2
# line3

"""
comment1
"""

x = 4
# print(x)
X = "sally"
print(x)
print(X)


a,b,c = "A","B","C"
print(a,b,c) # space, can connect different types, no math
print(a+b+c) # no space, must be the same type, do auto math

d = 1
D = "1"
# print(d,D)
# print(d+D)

x = 1
y = 1
print(x,y)
print(x+y)

x = y = z = "hello"
print(x,y,z)

fruits = ["apple","banana","cherry"]
x, y, z = fruits
print(x,y,z)

x = 5e10
print(x)

x = 3+5j
print(x)

a = 4
A = str(a)

rand = random.randrange(0,11,1) # [0,10) -> [0,9] ending is exclusive
print(rand)

a = """line1
line2
line3"""
print(a)

a = "Hello,World!"
# index always starts at zero
# H e l l o , W o r l d
# 0 1 2 3 4 5 6 7 8 9 10
print(a[1]) # -> name[index]
print(a[6])
print(a[11])
print(len(a)) # len:12, index:0-11

# for loops
for element in "hello_world": # for each index in "hello_world"
    print(element,end=", ") # char == character
print()

print("Hello" in a)
print("hello" in a)
print("abc" not in a)

