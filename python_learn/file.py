f = open("read.txt","r")
print(f.read())
text = open("C:/Users/Emerald Liu/Desktop/serverIP.txt")
print(text.read(17))
print(text.readline())
for x in text:
    print(text.readline())
f = open("read.txt","a")
f.write("Input new line\n")

f = open("newText.txt","x")



text.close()

