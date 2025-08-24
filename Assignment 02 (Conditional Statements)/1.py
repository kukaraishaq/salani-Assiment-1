#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
salry = int(input("salry :"))
year = int(input("years: "))
if year >5:
    bonus= salry *0.05
    print(bonus)
else:
    print("note eligable")