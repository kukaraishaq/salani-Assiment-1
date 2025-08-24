# Program to multiply two matrices

# Input dimensions
n = int(input("Enter number of rows of first matrix: "))
m = int(input("Enter number of columns of first matrix: "))

p = int(input("Enter number of columns of second matrix: "))
# Second matrix will automatically have m rows (for valid multiplication)

# Input first matrix A
print("\nEnter elements of first matrix (A):")
A = []
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"A[{i+1},{j+1}]: "))
        row.append(value)
    A.append(row)

# Input second matrix B
print("\nEnter elements of second matrix (B):")
B = []
for i in range(m):
    row = []
    for j in range(p):
        value = int(input(f"B[{i+1},{j+1}]: "))
        row.append(value)
    B.append(row)

# Multiply matrices
C = []
for i in range(n):
    row = []
    for j in range(p):
        sum_val = 0
        for k in range(m):
            sum_val += A[i][k] * B[k][j]
        row.append(sum_val)
    C.append(row)

# Display results
print("\nMatrix A:")
for row in A:
    print(*row)

print("\nMatrix B:")
for row in B:
    print(*row)

print("\nResult of A x B:")
for row in C:
    print(*row)
