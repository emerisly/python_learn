my_list = [1,2,3,5,4,4]
print(my_list)
print(my_list[0])
print(len(my_list))
list1 = ["str",1,False]
print(list1)
print(type(list1))

new_list = list(("str",1,False))
print(new_list)

my_list = [1,2,3,5,4,2]
print(my_list[-1])
print(my_list[0:-1]) # ending is exclusive
print(my_list[0:])
# my_list[1]=[1.3,1.6]
my_list[1:2]=[1.3,1.6]
print(my_list)
my_list.insert(len(my_list)-1,100)
print(my_list)

list1 = [1,2,3]
list2 = [5,6,7]
list1.append(4)
list1.extend(list2)
print(list1)
list1.pop(len(list1)-1)
print(list1)
list1.append(5)
print(list1)
list1.remove(5)
print(list1)

for i in range(8):
    print(i,end="")
print()
for i in list1:
    print(i,end="*")
print()
for i in range(len(list1)):
    print(list1[i],end="*")
print()
print("i =",i)
i = 0
while i<len(list1):
    print(list1[i],end=" ")
    i+=1
print()
[print(x,end="") for x in list1]
print()

list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)


list1 = [-1,2,5,-100,-4,20,49,-100,123]

def order(n):
    return abs(n)
list1.sort(key=order)
print(list1)

list1 = ["a","aaa","aaaaaa","aaaa"]

def length(n):
    return len(n)
list1.sort(key=length)
print(list1)
list1.reverse()
print(list1)

list2 = list(list1)
print(list2)

list1[0]="b"
print(list1,list2)
