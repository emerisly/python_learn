# HelloWorld
# hello_world

import random

"""
comments
"""

print("Hello World!")

x = 5
y = "5"
z = str(5)
ch = 'a'
print("x",type(x)) # after this line
print("y",type(y))
print("z",type(z))
print("ch",type(ch))

# , connect all kinds of types
# + connect only one type

if 5>2:
    print("Five > two")
    print("First Line")
    if 3>2:
        print("Three > two")
if 2>1:
    print("Second Line")


a, b, c = 1, 2, 3
print(a,b,c)

a = b = c = 10
print(a+b+c)
print(a,b,c)


fruits = ["apple","banana","cherry"]
x, y, z = fruits
print(x,y,z)

print(2/3)

complexNumber = 1j
print(type(complexNumber))

x = 3e5 # 3 * 10^5
print(x)


x1 = 2.1
x2 = int(x1)
print(x2)
x1 = 2.9
x2 = int(x1)
print(x2)
# python also use floor-rounding
print()

print(random.randrange(1,10)) # 1-9
print(random.randrange(0,10,2)) # 0,2,4,6,8

