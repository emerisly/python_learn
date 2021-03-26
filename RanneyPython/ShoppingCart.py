# add n to arr n times
def buildArr(arr, n, item):
    for i in range(n):
        arr.append(item)


# increase capacity by 3
def increaseSize():
    # append 3 to the array, which will be summed
    capacity.append(3)


# add a quantity of item to cart
def addToCart(item, unitPrice, quantity):
    # add the item to cart
    cart.append(item)
    individualPrice.append(unitPrice)
    # calculate total price for that item
    totalPrice = quantity * unitPrice
    # add it to the total price
    price.append(totalPrice)
    # record quantity of items purchased
    itemCount.append(quantity)


# print necessary info
def printCart():
    # use format function and map function to print result as a table
    # print("{:<8} {:<15} {:<12} {:<10}".format('item', 'unit price', 'quantity', 'total'))
    print("Item\t\tUnit Price\t\tQuantity\t\tTotal")
    # for formatted in map("{:<8} {:<17} {:<12} {:<10}".format, cart, individualPrice, itemCount, price):
    #    print(formatted)
    for n in range(len(cart)):
        print(cart[n],"\t\t\t",individualPrice[n],"\t\t\t",itemCount[n],"\t\t\t\t",price[n])
    # print current total
    print("Total Price of cart: $" + str(round(sum(price), 2)))


# main
# setting up arrays
cart = []
price = []
individualPrice = []
itemCount = []
# setting capacity up as an array to avoid error
capacity = [5]

# 1st item
# round(number,digit)
addToCart(input("What item do you want to buy? "),
          round(float(input("What is the unit price for that item? ")), 2),
          int(input("How many do you want? ")))
printCart()

# asks user to buy
while input("Do you want to continue shopping? ").lower() == "yes":
    # if the cart is not full
    if len(cart) < sum(capacity):
        # add item to cart
        addToCart(input("What item do you want to buy? "),
                  round(float(input("What is the unit price for that item? ")), 2),
                  int(input("How many do you want? ")))
        # print cart and total price after user put in an item
        printCart()
    # if the cart is full
    else:
        # notify user, then increase size
        print("Cart is full, increasing size for you")
        while len(cart) >= sum(capacity):
            increaseSize()
        print("Current cart size: " + str(sum(capacity)))

# after user stopped, ask for payment
print("Please pay: $" + str(round(sum(price), 2)))
