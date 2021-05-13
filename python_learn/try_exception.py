x=0
# print(x/0)
try:
    print(x/0)
except ZeroDivisionError:
    print("Cannot divide x by zero")
except NameError:
    print("Please name your x")

if x==1:
    raise Exception("x cannot be zero")

name = input("Please enter a name ")
print("Ok! your name is",name)
print(type(name))
number = int(input("Please enter a number "))
print(number,type(number))


