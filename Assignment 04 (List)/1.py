# Program to print alternate elements of a list

# Input from user (comma-separated values)
user_input = input("Enter elements of the list separated by spaces: ")

# Convert input into list
my_list = user_input.split()

print("Alternate elements are:")

# Print elements at even indexes
for i in range(0, len(my_list), 2):
    print(my_list[i])
