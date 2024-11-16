print("Welcome to the tip calculator.")
total_bill = float(input("What was your total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))


total_tip_amount = total_bill * (tip_percentage / 100)

split_amount = round((total_bill + total_tip_amount) / no_of_people, 2)

message = f"Each person should pay: ${split_amount}"

print(message)