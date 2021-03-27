tuple1 = ("green","blue","ruby")
print(tuple1)
print(tuple1[len(tuple1)-1])
# tuple a fixed array that cannot be changed once defined
# tuple1.append("white")
# print(tuple1)

fruits = ("apple","banana","cherry","blueberry")
(green,*yellow,red)=fruits
print(green,yellow,red)

new_fruits = fruits*2
print(new_fruits)
print(new_fruits.count("apple"))