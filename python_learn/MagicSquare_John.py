import re

# creating square
def createSquare(size):
    for i in range(size):
        new = []
        for j in range(size):
            new.append(1)
        square.append(new)

# returns the sum of a given row
# row -> which row
def sumRow(row):
    return sum(square[row])

# returns the sum of a given column
def sumCol(col):
    num = 0
    # square.length, (int) number -> java
    # len(square), int(number) -> python
    for k in range(len(square)):
        num += square[k][col]
    return num

# returns the sum of a diagonal
def sumMainDiag():
    ans = 0
    for i in range(len(square)):
    # square[row][col]
    # row = col
    # row -> i, square[i][i]
        ans += square[i][i]
    return ans

# returns the sum of another diagonal
def sumOtherDiag():
    ans = 0
    for i in range(len(square)):
        ans += square[i][len(square)-i-1]
    return ans

# returns if the square is magic
def magic():
    # store every sum in an array, and check if all elements in the array is equal
    # check diag, if yes, then check each row[i]=col[i]=row[0]=col[0]
    if sumMainDiag() == sumOtherDiag():
        for i in range(len(square)):
            if(sumRow(i)!=sumCol(i)):
                # print(sumRow(i),sumCol(i))
                return False
            if(sumRow(i)!=sumCol(0)):
                # print("2")
                return False
            if(sumRow(0)!=sumCol(i)):
                # print("3")
                return False
        # Diag == Diag && sumRow=sumCol
        return True
    # Diag != Diag
    # print("4")
    return False

# replaces the value in each position by a user input
def readSquare():
    square_string = []
    f = open("Magic_Square_Data.txt","r")
    size = int(f.readline())
    for ele in f:
        # each ele is one row in f
        list1 = list(re.split('\s+', ele))
        list1.pop()
        square_string.append(list1)
    for i in square_string:
        row = []
        for j in i:
            row.append(int(j))
        square.append(row)

# square[row][col] = int(input("Enter a number: "))
            
# print out the square
def printSquare():
    return print(square)


# main
# creating the empty square
square=[]
# make the square into given size
# createSquare()

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
