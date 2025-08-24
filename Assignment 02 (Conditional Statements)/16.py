# take input of age of 3 people by user and determine oldest and youngest among them.
age1 = int(input("Eanter yor age of first person : "))
age2 = int(input("Eanter yor age of second person : "))
age3 = int(input("Eanter yor age of third person : "))
# Check oldest
if(age1>age2 and age1>age3 ):
    oldest =age1
elif(age2>age1 and age2>age3 ):
    oldest =age2
elif(age3>age2 and age3>age1 ):
    oldest =age3
print ("The oldest person",oldest)
