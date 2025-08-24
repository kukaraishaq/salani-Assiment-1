# Program to print first 6 terms of a geometric progression

first_term = 2
common_ratio = 3
terms = 6

print("The first", terms, "terms of the geometric sequence are:")

for i in range(terms):
    term = first_term * (common_ratio ** i)
    print(term, end=" ")
