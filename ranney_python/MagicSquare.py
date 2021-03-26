# creating square
def createSquare(size):
    # check if size is valid
    if size <= 0:
        print("Error in size")
    else:
        # create square of given size (all value is 1)
        for i in range(size):
            new = []
            for j in range(size):
                new.append(1)
            square.append(new)
            
# returns the sum of a given row
def sumRow(row):
    return sum(square[row])

# returns the sum of a given column
def sumCol(col):
    num=0
    for k in range(len(square)):
        num += square[k][col]
    return num

# returns the sum of a diagonal
def sumMainDiag():
    main_diagonal = 0
    for o in range(len(square)):
        # going from left to right and up to down
        main_diagonal += square[o][o]
    return main_diagonal

# returns the sum of another diagonal
def sumOtherDiag():
    other_diagonal = 0
    for o in range(len(square)):
        # (len(square)-1-o) decreases as o increases, so going from right to left and up to down
        other_diagonal += square[o][len(square)-1-o]
    return other_diagonal

# returns if the square is magic
def magic():
    # check if diagonals are equal
    if sumOtherDiag() == sumMainDiag():
        for c in range(len(square)):
            # check if sum for a row is equal to sum for a column
            if sumRow(c) != sumCol(c):
                return False
            # check if the sum for every row is equal
            elif sumRow(c) != sumRow(0):
                return False
            # check if the sum for every column is equal
            elif sumCol(c) != sumCol(0):
                return False
            # if everything equal, return true
            else:
                return True
    # if not equal, return false
    else:
        return False
    
# replaces the value in each position by a user input
def readSquare():
    for row in range(len(square)):
        for col in range(len(square)):
            square[row][col] = int(input("Enter each number in the square: "))
            
# print out the square
def printSquare():
    for m in range(len(square)):
        for n in range(len(square)):
            print(square[m][n], end=" ")
        print()


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
