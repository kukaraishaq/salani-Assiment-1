# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
year =int(input("Eanter year : "))
# program to check if a year is leap year or not.
if (year%4==0 and year%100 != 0) or (year%400==0):
    print("This is leap year")
else:
    print("This is not leap year")


