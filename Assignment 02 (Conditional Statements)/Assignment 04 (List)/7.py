def capitalize_words(sentence):
    words = sentence.split()   # Split sentence into words
    result = ""

    for word in words:
        # Capitalize first character manually
        capitalized = word[0].upper() + word[1:].lower() if len(word) > 0 else ""
        result += capitalized + " "

    return result.strip()   # Remove last extra space


# Input from user
sentence = input("Enter a sentence: ")
new_sentence = capitalize_words(sentence)

print("Converted sentence:", new_sentence)
