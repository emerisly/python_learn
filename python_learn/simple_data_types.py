poem = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
poem = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua'''
print(poem)

s = "Hello World"
print("string is actually an array! ",s[0])

for x in s:
    print(x,end="")

print("*************hello_world_",end="")

# SOPln -> print(  )
# SOP -> print(  ,end="")

print("\nlength of s is: ",len(s))

flag = "Hello" in s # case sensitive
print(flag)
print("hello" in s)

if "World" in s:
    print("Yes s contains World")

if "World" not in s:
    print("No s does not contain World")

s = "hello world"
print(s[0])
print(s[0:5]) # exclusive
print(s[0:11])
print(s[:5])
print(s[5:])

s = "    today is a good day!    "
print(s[-4:-1])

print(s.upper())
# print(len(s))
s = s.strip()
print(s)
print(s.replace(" ",""))
print(s.split(" "))

number = 47
fav_number = 7
name = "My name is {}, and my favorite number is {}"
print(name.format(number,fav_number))

name = "My name is"
print(name,number)

x = '\101\102\103'
print(x)

x = '\x41\x42\x43'
print(x)

s = "123"
print(s.isdigit())
print(s.isalpha())

print(3**3)
print(2/3)
print(2//3)


for x in range(5):
    print("hello_world_",end="")