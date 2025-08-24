# Program to generate first n terms of the series (squares of natural numbers)

# Input from user
n = int(input("Enter a number: "))

print("The first", n, "terms of the series are:")

for i in range(1, n + 1):
    print(i * i, end=" ")
