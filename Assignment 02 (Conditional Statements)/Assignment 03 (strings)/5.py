# Program to shift string one position to the left

# Input from user
text = input("Enter a string: ")

# Check if string has more than 1 character
if len(text) > 1:
    new_text = text[1:] + text[0]
else:
    new_text = text  # if only 1 char, no change

# Display result
print("New string:", new_text)

