def my_function1():
    print("Hello from a function\n")

def my_function(name):
    print(name + " Refsnes")


my_function("Emil")
my_function1()


def my_function(country="Country Unknown"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()

print()

def my_function(food, fruit):
    for x in food:
        print(x)
    for y in fruit:
        print(y)


food = ["bread", "noodles", "pizza"]
fruits = ["apple", "banana", "cherry"]
my_function(food, fruits)

print("\n************\n")

# overriding methods
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
print()

def my_lista(kids):
    print("The youngest child is " + kids[2])

# ues * to refer to store the inputed value into this var
def my_listb(*kids):
    print("The youngest child is " + kids[2])

list1=["a","b","c"]
my_lista(list1)

my_listb("Emil", "Tobias", "Linus")


# *kids will be a tuple

def add_backwards(n):
    if n>0:
        ans= n+add_backwards(n-1)
        print("+",n,"=",ans)
    else:
        ans=0
    return ans

add_backwards(3)


print("\n***************\n")

# lambda arguments : expression
# only one expression
# use them as an anonymous function inside another function

product = lambda a, b: a * b
print(product(5, 6))


# first func indicate var in the parameter
# second func indicate the other var
def my_func(n):
    return lambda a: a*n*n

my_doubler = my_func(2)
print(my_doubler(10))