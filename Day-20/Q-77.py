# This is a program for matrix multiplication.


r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication is not possible")
else:
    mat1 = []
    mat2 = []

    print("Enter first matrix:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        mat1.append(row)

    print("Enter second matrix:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        mat2.append(row)

    mat3 = []

    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += mat1[i][k] * mat2[k][j]
            row.append(total)
        mat3.append(row)

    print("Resultant Matrix:")
    for row in mat3:
        print(row)
