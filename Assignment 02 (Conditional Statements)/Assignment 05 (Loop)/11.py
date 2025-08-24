# Program to calculate sum of integers from 1 to n

# Input from user
n = int(input("Enter a positive integer: "))

# Initialize sum
total = 0

# Loop from 1 to n
for i in range(1, n + 1):
    total += i

# Display result
print("The sum of numbers from 1 to", n, "is:", total)
