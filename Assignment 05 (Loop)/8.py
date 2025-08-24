# Program to print multiplication table of a number

# Input from user
n = int(input("Enter a number: "))

print("Multiplication Table of", n)

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
