# Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

Numofch = int(input("Number of classes held: "))
attended = int(input("Number of classes attended: "))
#He has medical cause or not
cause =input("You has medical cause or not only answer in Y and N")

# Correct calculation using division
percentage = (attended / Numofch) * 100

print(f"Percentage of classes attended: {percentage:.2f}%")

# Is student allowed to sit in exam or not
if percentage >=75:
    print("Student will NOT be allowed to sit in exam because his/her attendance is less than 75%.")
elif cause.upper()==("Y"):
    print("Student will be allowed to sit in exam due to medical cause")
else:
    print("Student will be allowed to sit in exam.")




