# Program to calculate running total of 5 numbers

total = 0  # initialize sum

for i in range(5):
    num = int(input("Enter a number: "))
    total += num

print("The final running total is:", total)
