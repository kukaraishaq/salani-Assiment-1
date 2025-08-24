# Program to find largest number in a list without using max()

# Take list input from user
user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]  # Convert input into integer list

# Assume first element is the largest
largest = num_list[0]

# Loop through list to find largest
for num in num_list:
    if num > largest:
        largest = num

# Display result
print("The largest number in the list is:", largest)
