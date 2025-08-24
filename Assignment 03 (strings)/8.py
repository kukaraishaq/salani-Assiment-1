# Program to display shifting pattern

word = "SHIFT"

# Loop through length of word
for i in range(len(word)):
    # Rotate string by i positions
    rotated = word[i:] + word[:i]
    print(rotated)
