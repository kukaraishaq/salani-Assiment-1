# Program to find sum of each row in a matrix

# Input matrix size
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# Initialize empty matrix
matrix = []

# Input matrix elements row by row
print("Enter the elements row by row:")
for i in range(m):
    row = []
    for j in range(n):
        value = int(input(f"Enter element at position [{i+1},{j+1}]: "))
        row.append(value)
    matrix.append(row)

# Display matrix
print("\nMatrix:")
for row in matrix:
    print(*row)

# Calculate sum of each row
for i in range(m):
    row_sum = 0
    for j in range(n):
        row_sum += matrix[i][j]
    print(f"Sum of row {i+1} = {row_sum}")
