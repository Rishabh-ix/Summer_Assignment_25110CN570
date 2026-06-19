# This is a program to subtract two matrix.


row= int(input("Enter number of rows: "))
coloumn = int(input("Enter number of coloumn: "))
mat1 = []
mat2 = []
print("Enter first matrix: ")
for i in range(row):
    rows = []
    for j in range(coloumn):
        value = int(input(f"Enter element [{i}][{j}]: "))
        rows.append(value)
    mat1.append(rows)

print("Enter second matrix: ")
for i in range(row):
    rows = []
    for j in range(coloumn):
        value = int(input(f"Enter element [{i}][{j}]: "))
        rows.append(value)
    mat2.append(rows)
mat3 = []
for i in range(row):
    add = []
    for j in range(coloumn):
        add.append(mat1[i][j] - mat2[i][j])
    mat3.append(add)
        
print("Addition of matrix is:")
for add in mat3:
    print(add)

