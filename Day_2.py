# DAY2
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
#print(bill)
PerTip = float(input("How much tip would u like to give? 10,12, or 15? "))
#print(PerTip)
div = float(input("How many people to split the bill among? "))
tip = (bill/100) * PerTip
each = (bill + tip) / div

result =  round(each,2)

#print(result)

print(f"Each person should pay: {result}")

