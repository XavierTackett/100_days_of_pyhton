#Data Types
print("Hello welcome to the tip calculator.")

#Questions
bill = float(input("How much was the total bill? "))
guest = int(input("How many guest are you going to be splitting the bill with? "))
tip_percent = int(input("What percentage would you like to tip? "))

#Calculations
tip_percent = tip_percent / 100
tip = float(tip_percent) * (bill)
bill = (bill) + float(tip)
bill_split = bill / guest          
final_bill = "{:.2f}".format(bill_split)

#Bill split between guest with tip
print(f"Each person should pay: ${final_bill}")
