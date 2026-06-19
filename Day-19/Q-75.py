# This is a program to find transpose of a matrix.


row= int(input("Enter number of rows: "))
coloumn = int(input("Enter number of coloumn: "))
mat1 = []
mat2 = []
print("Enter matrix: ")
for i in range(row):
    rows = []
    for j in range(coloumn):
        value = int(input(f"Enter element [{i}][{j}]: "))
        rows.append(value)
    mat1.append(rows)

for i in range(coloumn):
    rows = []
    for j in range(row):
        rows.append(mat1[j][i])
    mat2.append(rows)

        
print("Transpose of matrix is:")
for rows in mat2:
    print(rows)

