# tuple's value cannot be modified
# is not sorted
x = (1, 5, 3, 4, 8)
# did not sorted
print(x)
print(x[0])
y = (1, 'max', 1.6)
z = x + y
print("z = ",z)
# remember to add comma
a = ('hi',) * 5
print("a = ", a)
print("x = ", x)
print("find max: ", max(x))
del x
# print(x)

# tuple cannot be copied


# vs list
list1 = [1, 5, 10, 3]
print(list1)
