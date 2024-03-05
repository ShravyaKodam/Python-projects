print("Welcome to the tip calculator")
bill=int(input("What is the total bill? "))
tip=int(input("What percentage tip would you like to give? \n 10, 12, or 15?"))
persons=int(input("How many people to split the bill? "))
percentageOfTip=(tip*bill)/100
personPay=round((bill+percentageOfTip)/persons,2)
print(f"Each person should pay: ${personPay}")