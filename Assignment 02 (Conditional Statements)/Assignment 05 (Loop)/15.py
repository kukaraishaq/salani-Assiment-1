# Program to calculate power without using ** or math.pow()

# Input from user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1

if exponent > 0:
    for _ in range(exponent):
        result *= base
elif exponent < 0:
    for _ in range(-exponent):   # loop for absolute value of exponent
        result *= base
    result = 1 / result          # reciprocal for negative exponent
# if exponent == 0, result stays 1

print(base, "raised to the power", exponent, "is:", result)
