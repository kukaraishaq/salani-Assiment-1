# Program to count uppercase, lowercase, digits, and whitespace

# Read string from user
text = input("Enter a string: ")

# Initialize counters
uppercase = 0
lowercase = 0
digits = 0
whitespace = 0

# Loop through each character
for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        whitespace += 1

# Display results
print("Number of uppercase letters:", uppercase)
print("Number of lowercase letters:", lowercase)
print("Number of digits:", digits)
print("Number of whitespace characters:", whitespace)
