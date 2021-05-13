mytuple = ("apple","banana",'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(myit)

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))

if 1<2:
    global x
    x = 3
    print(x)
print(x)

