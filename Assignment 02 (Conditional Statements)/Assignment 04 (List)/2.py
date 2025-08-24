# Program to reverse a list without using reverse()

# Take list input from user
user_input = input("Enter elements separated by spaces: ")
my_list = user_input.split()   # Convert input string into list

# Reverse manually
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

# Display result
print("Original list:", my_list)
print("Reversed list:", reversed_list)
