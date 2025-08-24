# Program to count vowels in a string

# Accept input from user
text = input("Enter a string: ")

# Initialize counter
vowel_count = 0

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
for char in text:
    if char in vowels:
        vowel_count += 1

# Display result
print("Number of vowels in the string:", vowel_count)
