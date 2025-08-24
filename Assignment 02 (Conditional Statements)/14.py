# Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR"
age = int(input("Enter age : "))
gander =input("Eanter your gabder M/F : ")
marital_status =input("Eanter your marital status : ")
# if employee is female, then she will work only in urban areas.
if (gander==("F")):
    print("You will work only in urban areas")
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
elif (gander=="M" and 20 <= age <= 40):
    print("You may work in anywhere")
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
elif (gander=="M" and 40 <= age <=60):
    print("You will work in urban areas only.")
# And any other input of age should print "ERROR"
else:
    print("ERROR")

