import re

f = open("Magic_Square_Data.txt","r")
size = int(f.readline())
print("square size: ",size)
list2d = []
for x in f:
    # \s white space, + separate al all white spaces
    # re.split('__',var_name)
    list1 = list(re.split('\s+', x))
    list1.pop()
    # print(type(list1[0]))
    # print(list1)
    # print(type(list1))
    list2d.append(list1)
    # print(list2d)
# print(list2d)

list2d_int = []
for i in list2d:
    row = []
    for j in i:
        row.append(int(j))
    list2d_int.append(row)
print("int list is: ",list2d_int)

# print(int(list2d[0][0]))

f.close()