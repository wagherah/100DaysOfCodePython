# Project Day 2

print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15"))
people = int(input("How many people to split the bill?"))
per_head = (total_bill + ((tip_percentage/100)*total_bill)) / people
per_head = round(per_head, 2)
print(f"Each person should pay: ${per_head}")
