# creating square
def createSquare(size):
            
# returns the sum of a given row
def sumRow(row):

# returns the sum of a given column
def sumCol(col):

# returns the sum of a diagonal
def sumMainDiag():

# returns the sum of another diagonal
def sumOtherDiag():

# returns if the square is magic
def magic():
    
# replaces the value in each position by a user input
def readSquare():
            
# print out the square
def printSquare():


# main
# creating the empty square
square=[]
# make the square into given size
createSquare(int(input("please enter the size of square: ")))
# replaces the value at each position
readSquare()

# check if the square is magic
if magic():
    print("the square is a magic square")
else:
    print("the square is not a magic square")
# print out the square
print("The square is: ")
printSquare()
