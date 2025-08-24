# Program to validate password

password = input("Enter a password: ")

# Conditions
has_upper = False
has_lower = False
has_digit = False

# Check each character
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

# Validation
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Password is valid ✅")
else:
    print("Password is invalid ❌")
    print("Requirements:")
    print("- At least 8 characters long")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one numeric digit")
