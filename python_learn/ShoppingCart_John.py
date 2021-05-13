
# add n to arr n times
def buildArr(arr, n, item):
 for x in range (n):
  arr+=item


# increase capacity by 3
def increaseSize(capacity):
 capacity += 3

totalPrice = {}
# add a quantity of item to cart
def addToCart(item, unitPrice, quantity):
 cart = []
 cart += item
 totalPrice = unitPrice * quantity * cart


# print necessary info
def printCart():
 print (totalPrice)







# main
# setting up arrays
cart = []
price = []
individualPrice = []
itemCount = []
# setting capacity up as an array to avoid error
capacity = [5]
size = 1


name = ""
unitPrice = 0.0
quan = 0


# ask for 1st item
name=input("What item do you want to buy? ")
cart.append(name)
unitPrice=(float(input("What is the unit price for that item? ")), 2)
individualPrice.append(unitPrice)
quan=int(input("How many do you want? "))
itemCount.append(quan)
price.append(unitPrice*quan)
print("Item\tUnit Price\tQuantity\tTotal")
for i in range(size):
 # print(type(i))
 # print(i)
 print(cart[i],"\t",individualPrice[i],"\t\t\t",itemCount[i],"\t\t",price[i])



# asks user to buy
# Hint: use while loop
#
# input("Do you want to continue shopping? ").lower() == "yes"



# after user stopped, ask for payment
print("Please pay: $")
print(type(price))
print(sum(price))
# print(str(round(sum(price), 2)))