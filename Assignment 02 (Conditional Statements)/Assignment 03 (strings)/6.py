# Program to print initials without using split()

# Input from user
name = input("Enter your full name (First Middle Last): ")

# Initialize result with the first character
initials = name[0].upper() + ". "

# Loop through the string
for i in range(len(name)):
    if name[i] == " " and i + 1 < len(name):
        initials += name[i+1].upper() + ". "

# Display result
print("Initials:", initials)
