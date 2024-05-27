print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $ "))
tipPercentage = float(input("How much tip would you like to give? 10, 12, or 15?"))
totalBillWithTip = totalBill + (totalBill * tipPercentage / 100)
splitBill = int(input("How many people to split the bill?"))
billPerPerson = totalBillWithTip / splitBill
print(f"Each person should pay: ${billPerPerson:.2f}")

