# Program to check if a string is palindrome

# Input from user
text = input("Enter a string: ")

# Assume it is palindrome
is_palindrome = True

# Compare characters from start and end
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break

# Display result
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")
