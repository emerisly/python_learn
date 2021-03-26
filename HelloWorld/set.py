# all set values are unique
# is sorted
a = {1, 2, 5, 4, 7, 9, 2}
print(a)
a.add(10)
print("add 10: ", a)
a.update([15, 18, 17, 14])
print(a)

for ele in a:
    print(type(ele), end=" ")
print()

a.remove(18)
# a.remove(11)
a.discard(17)
a.discard(11)
# discard does not return error if no such value found
print(a)
# pop out random if it's string, pop out first if int
print("pop = ", a.pop())
print(a)

name = {'max', 'tom', 'den'}
print("set is: ", name)
name.clear()
print("set is now", name)
del name
# print("name set is now", name)

name = set(('max', 'tom', 'den'))
print("name set is ", name)
print("pop = ", name.pop())
z = set([1, 2, 3, 4])
print(z)

a = {1, 2, 5, 7, 9, 10, 13}
b = {10, 11, 12, 13, 14, 15}
print("union", a|b)
print("union", a.union(b))
print("intersection", a&b)
print("intersection", a.intersection(b))
print(a,b)
print("a difference b", a-b)
print("b difference a", b-a)

# set has no index
# no methods with index

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
thisset.update("1","2")
print(thisset)