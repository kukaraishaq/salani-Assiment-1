# Program to calculate sum of reciprocals from 1 to N

# Input from user
n = int(input("Enter a positive integer: "))

# Initialize sum
total = 0

# Loop to calculate reciprocals
for i in range(1, n + 1):
    total += 1 / i

# Display result (rounded to 2 decimal places)
print("The sum of reciprocals from 1 to", n, "is:", round(total, 2))
