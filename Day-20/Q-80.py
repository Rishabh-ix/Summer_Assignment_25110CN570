# This is a program to find coloumn-wise sum.




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

for i in range(coloumn):
    total = 0 
    for j in range(row):
        total = total + mat1[j][i]
    print(f"Sum of coloumn {i+1} is:",  total)
    