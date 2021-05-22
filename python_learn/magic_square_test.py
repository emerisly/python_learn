square = []
# square.append(int(input("Enter a number: ")))
# print(square)
size = int(input("Enter a number: "))
for i in range(size):
    # crate new array called new (row)
    new = []
    # fill out new array with size col's of 1
    for j in range(size):
        new.append(0)
    # append each row to square
    square.append(new)
print(square)