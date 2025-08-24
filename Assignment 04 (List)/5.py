# Program to delete a given word from a string

# Input string from user
text = input("Enter a string: ")

# Input word to delete
word_to_delete = input("Enter the word you want to delete: ")

# Remove the word (only the first occurrence)
new_text = text.replace(word_to_delete, "", 1)

# Remove any extra spaces caused by deletion
new_text = " ".join(new_text.split())

print("String after deleting the word:", new_text)
