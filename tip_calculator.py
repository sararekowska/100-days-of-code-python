print("Welcome to the Tip Calculator!")

total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

with_tip = percentage / 100 * total + total
result = round(with_tip / people, 2)



print(f"Each person should pay: ${result}")