# Program to add two matrices of size n x m

# Input size of matrix
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Input first matrix
print("\nEnter elements of first matrix:")
A = []
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"A[{i+1},{j+1}]: "))
        row.append(value)
    A.append(row)

# Input second matrix
print("\nEnter elements of second matrix:")
B = []
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"B[{i+1},{j+1}]: "))
        row.append(value)
    B.append(row)

# Add matrices
C = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# Display result
print("\nMatrix A:")
for row in A:
    print(*row)

print("\nMatrix B:")
for row in B:
    print(*row)

print("\nSum of Matrices (A + B):")
for row in C:
    print(*row)
