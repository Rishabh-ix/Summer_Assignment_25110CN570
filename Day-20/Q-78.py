# This is a program to check symmetric matrix.


row= int(input("Enter number of rows: "))
coloumn = int(input("Enter number of coloumn: "))
mat1 = []
if(row != coloumn):
    print("This is not a symmetric matrix")
else:
   print("Enter matrix: ")
   for i in range(row):
    rows = []
    for j in range(coloumn):
        value = int(input(f"Enter element [{i}][{j}]: "))
        rows.append(value)
    mat1.append(rows)
   flag = 0 
   for i in range(row):
    for j in range(coloumn):
        if(mat1[i][j] != mat1[j][i]):
            flag = 1
            break
    if(flag == 1):
       break

   if(flag == 0):
    print("This is a symmetric matrix")
   else:
    print("This is not a symmetric matrix")
