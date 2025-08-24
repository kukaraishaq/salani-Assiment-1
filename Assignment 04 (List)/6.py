# Program to convert date format mm/dd/yyyy to Month dd, yyyy

# Input date from user
date = input("Enter a date in mm/dd/yyyy format: ")

# Split into parts
month, day, year = date.split("/")

# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Convert month number to name
month_name = months[int(month) - 1]

# Print formatted date
print(f"{month_name} {int(day)}, {year}")
