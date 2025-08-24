#A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quat =int(input("eanter amount : "))
unit =100
total_bill =quat*unit
if total_bill>1000:
    discount =total_bill*0.10
    total_bill-=discount
    print("you get 10persent discount")
    print("total bill:" ,total_bill)

    
