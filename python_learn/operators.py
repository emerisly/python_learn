x = 5
y = x >> 2 # y = x//n (2^n)
z = x << 2 # z = x*2
print(y,z)

if (x>1 and x<10):
    print("OK")

if 1 < x < 10:
    print("x>1 and x<10")

if (x<0 or y<0):
    print("x>1 or y<1")
else:
    print("none of them <0")

if (x is y):
    print("x=5")

if (x is not y):
    print("x!=5")

arr = [1,2,3,4,5]
if (x in arr):
    print("x is in arr")

binary1 = 100
binary2 = 101
binary3 = binary1 & binary2
binary4 = binary1 | binary2
print(binary3,binary4)
binary5 = binary1 ^ binary2
print(binary5)

print(x==y)

print(bool("Hello"))
print(bool(""))
print(bool(15))
print(bool(0))

def fun():
    return True

value = fun();
print("return",fun())
print(value)
print("is value a bool?",isinstance(value,bool))