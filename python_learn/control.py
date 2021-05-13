if 1>3:
    print("1<3")
elif 2>3:
    print("2<3")
else:
    print("idk")

print("Yes") if 1<2 else print("No")

a = 100
b = 100
print("A") if a > b else print("=") if a < b else print("B")


i = 1
while i < 6:
    print(i,end="")
    i += 1 # python does not have i++
print()

i = 0
while i < 10:
    i+=1
    # print("i=",i,end="    ")
    if i % 2 != 0:
        continue
    print(i,end="")
else:
    print("i>=10")


fruit = ["A","B","C"]
for x in fruit:
    print(x)
    if x == "B":
        break

def func(*list1):
    print(list1[0])

func(1,2,3)

x = lambda a : a + 10
print(x(0))

power = lambda input : input**2
print(power(1),power(2),power(3))
