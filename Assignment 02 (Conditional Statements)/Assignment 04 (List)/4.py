# Program to rotate list elements to the right by one position

# Take list input from user
user_input = input("Enter elements separated by spaces: ")
my_list = user_input.split()

# Rotate: last element moves to first position, others shift right
rotated_list = [my_list[-1]] + my_list[:-1]

# Display result
print("Original list:", my_list)
print("Rotated list :", rotated_list)
