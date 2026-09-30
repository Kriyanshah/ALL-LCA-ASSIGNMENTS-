# Addition of matrix
rows = int(input("Enter the no. of rows: "))
cols = int(input("Enter the no. of cols: "))

print("Enter the elements of the matrix A: " )
A=[]
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter A[{i}][{j}] : "))
        row.append(value)
    A.append(row)

print("Enter the elements of the matrix B: " )
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter B[{i}][{j}] : "))
        row.append(value)
    B.append(row)

import numpy as np
A = np.array(A)
B = np.array(B)

C = A+B
print("\nMatrix A: ")
print(A)
print("\nMatrix B: ")
print(B)
print("\nMatrix A+B: ")
print(C)





