# This is a program to find row-wise sum.


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

for i in range(row):
    total = 0 
    for j in range(coloumn):
        total = total + mat1[i][j]
    print(f"Sum of row {i+1} is:",  total)
    