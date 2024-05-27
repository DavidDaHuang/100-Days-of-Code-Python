print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15?"))
total_bill_with_tip = totalBill + (totalBill * tipPercentage / 100)
split_bill = int(input("How many people to split the bill?"))
bill_per_person = totalBillWithTip / splitBill
print(f"Each person should pay: ${billPerPerson:.2f}")

