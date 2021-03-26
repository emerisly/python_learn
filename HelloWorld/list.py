# lists are like array
# is not sorted
x = [3, 5, 4, 9, 7, 10]
print(x)
print(x[0])
print(x[3])
y = ['max', 1, 15.5, [3, 2]]
print(y[3])
print(len(y))
y.insert(1, 'tom')
print(y)
y.remove('tom')
print(y)
del y[0]
print(y)
# pop removes the last index of a list
print(y.pop())
print("pop", y)
del y
# error print(y)
x.clear()
print("x is now", x)
x.append(1)
print("x is now", x)
y = x.copy()
print("y is now", y)
y.append(1)
print("how many 1 in y:", y.count(1))

y=[1, 2, 3, 4]
for x in y:
    print(x)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
list1.extend(list2)
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list = [0] * 5
print(list)
listc= [0, 0, 0, 0, 0]
print(listc)

set1={1,2,3}
print("set1 pop =", set1.pop())

set2={"1","2","3"}
print("set2 pop = ", set2.pop())

number=[1,2,3]
number.pop()
print(number)

wtf=["A","B","C"]
wtf.pop();
print(wtf)