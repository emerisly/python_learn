import math

"""
+
-
*
/ (one decimal)
// (floor)
%
** (power)


Reserved Words
and del for is raise asert elif from lambda return
break else global not try class except if or while
continue exec import pass yield def finally in print

dir (__builtins__)
help(xxx)

"""


def pf():
    print("py is" + x)


x = "awesome"
pf()

# use comma to separate different types
x = 5
y = "John"
print(x, y)

print(4 / 2)  # kept one decimal

complexNum = 2j
print(complexNum, type(complexNum))

num = 10e10
print(num)  # kept one decimal

num = 233
myFloat = float(num)
print(myFloat, type(myFloat))
myInt = int(myFloat)
print(myInt, type(myInt))

x = 1
y = 2
print("{0}*{1}={2}".format(x, y, x * y))

print("Hello", "World", "!", sep="---")

"""
%s string
%d int
%f float
%.2f limit digit
"""

name = "Emerald"
print("Hello %s" % name)

number = 3.141592653
print("%0.4f" % number)  # rounding up

# input value
"""
value1=int(input("Enter some value:"))
print("value squared = %d"%(value1*value1))
value2=float(input("Enter some value:"))
print("value rounded is %0.3f"%value2)
print(value1**2,pow(value1,2),value2)
value=input("input again ")
print(value)
"""

x = 2
print(x ** 7)
print(pow(2, 7))
print(len("Hello"))

print(math.sqrt(100))

"""
x=float(input("input 1: "))
y=float(input("input 2: "))
z=float(input("input 3: "))
print("The max is: ",max(x,y,z))
input("Press any key to continue")
"""

"""
python - interpret language, no need to compile
source code directly to output
"""

x = "Hello's World"
y = 'Hello\'s World'
print(x, y)

# input()

x = "hello"
y = "   Hello    "
z = "Hello How are you"
print(x.upper())
print("print part",x[0:3])
print("strip",y.strip())
print(x.islower())
print(y.isupper())
print("replace",y.replace(" ", "_"))
print("split",z.split(" "))
print(x * 10)

