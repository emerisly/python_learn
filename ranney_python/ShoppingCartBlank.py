# add n to arr n times
def buildArr(arr, n, item):


# increase capacity by 3
def increaseSize():


# add a quantity of item to cart
def addToCart(item, unitPrice, quantity):



# print necessary info
def printCart():






# main
# setting up arrays
cart = []
price = []
individualPrice = []
itemCount = []
# setting capacity up as an array to avoid error
capacity = [5]


name = ""
unitPrice = 0.0
quan = 0

name=input("What item do you want to buy? "),
unitPrice=round(float(input("What is the unit price for that item? ")), 2),
quan=int(input("How many do you want? "))
print(name,unitPrice,quan)

# ask for 1st item


# asks user to buy
# Hint: use while loop
#
# input("Do you want to continue shopping? ").lower() == "yes"



# after user stopped, ask for payment
print("Please pay: $" + str(round(sum(price), 2)))
