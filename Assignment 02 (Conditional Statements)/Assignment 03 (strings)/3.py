# Program to swap first and last characters of a string

# Input from user
text = input("Enter a string: ")

# If string length is greater than 1
if len(text) > 1:
    new_text = text[-1] + text[1:-1] + text[0]
else:
    new_text = text  # If only one character, keep it as is

# Display result
print("New string:", new_text)

