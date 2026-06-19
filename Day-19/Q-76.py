# This program finds diagonal sum of a matrix.


row= int(input("Enter number of rows: "))
coloumn = int(input("Enter number of coloumn: "))
mat1 = []
print("Enter matrix: ")
for i in range(row):
    rows = []
    for j in range(coloumn):
        value = int(input(f"Enter element [{i}][{j}]: "))
        rows.append(value)
    mat1.append(rows)
sum = 0
for i in range(row):
    for j in range(coloumn):
        if(i==j):
            sum = sum + mat1[i][j]
 
print("Diagonal sum of matrix is: ")
print(sum)