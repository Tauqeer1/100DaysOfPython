print("Welcome to the pizza deliveries!")

size = input("What size of Pizza do you want? S, M, or L ")
add_pepperoni = input('Do you want pepperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')


# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# pepperoni_small_pizza = 2
# pepperoni_medium_or_large_pizza = 3

# extra_cheese = 1

bill = 0

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
    
if add_pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f"Your final bill is: ${bill}")