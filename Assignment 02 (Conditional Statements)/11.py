# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print percentage of class attended
# Is student allowed to sit in exam or not.

Numofch = int(input("Number of classes held: "))
attended = int(input("Number of classes attended: "))

# Correct calculation using division
percentage = (attended / Numofch) * 100

print(f"Percentage of classes attended: {percentage:.2f}%")

# Is student allowed to sit in exam or not
if percentage < 75:
    print("Student will NOT be allowed to sit in exam because his/her attendance is less than 75%.")
else:
    print("Student will be allowed to sit in exam.")
