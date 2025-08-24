# Program to print first 8 terms of an arithmetic progression

first_term = 3
common_diff = 4
terms = 8

print("The first", terms, "terms of the AP are:")

for i in range(terms):
    term = first_term + i * common_diff
    print(term, end=" ")
