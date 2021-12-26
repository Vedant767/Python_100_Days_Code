total_bill = float(input("What was the total bill?"))
tip_per = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_people = int(input("How many people to split the bill?"))

tip_total_bill = total_bill * tip_per / 100
bill_after_tip = total_bill + tip_total_bill
print(f"Each person should pay: {round(bill_after_tip/number_of_people, 2)}")