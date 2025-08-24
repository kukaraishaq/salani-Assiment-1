# Write a program to calculate the electricity bill (accept number of unit from user) according to the following
#  criteria : Unit Price
# uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example  
# if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than 
# total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750
unit =int(input("Eanter units : "))
if (unit<=100):
    bill =0
elif (unit<=300):
    bill= unit*5
else:
    bill= unit*10
print("Total bill" ,bill )


