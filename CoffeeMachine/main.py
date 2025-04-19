MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 300,
    "money": 0
}

coins_value = {
    "penny": 0.01,
    "dime": 0.10,
    "nickel": 0.05,
    "quarter": 0.25
}

def calculate_inserted_amount(quarters_count, dimes_count, nickels_count, pennies_count):
    return quarters_count * coins_value['quarter'] + dimes_count * coins_value['dime'] + nickels_count * coins_value['nickel'] + pennies_count * coins_value['penny']

def check_sufficient_resources(type_of_coffee):
    ingredients = MENU[type_of_coffee]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def check_sufficient_amount(type_of_coffee, total_amount):
    cost_of_coffee = MENU[type_of_coffee]["cost"]
    if cost_of_coffee > total_amount:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

def calculate_remaining_amount(type_of_coffee, total_amount):
    cost_of_coffee = MENU[type_of_coffee]["cost"]
    return round(total_amount - cost_of_coffee, 2)

def update_revenue(type_of_coffee):
    resources["money"] += MENU[type_of_coffee]["cost"]

def update_resources(type_of_coffee):
    ingredients = MENU[type_of_coffee]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

is_machine_on = True

while is_machine_on is True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_type == 'off':
        is_machine_on = False
    elif coffee_type == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Revenue: ${resources['money']}")
    elif coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino':
        is_sufficient_resources = check_sufficient_resources(coffee_type)

        if is_sufficient_resources is True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            amount_inserted = calculate_inserted_amount(quarters, dimes, nickels, pennies)

            is_sufficient_amount = check_sufficient_amount(coffee_type, amount_inserted)
            if is_sufficient_amount is True:
                amount_remaining = calculate_remaining_amount(coffee_type, amount_inserted)
                update_revenue(coffee_type)
                update_resources(coffee_type)
                print(f"Here is your ${amount_remaining} in change.")
                print(f"Here is your {coffee_type} ☕️. Enjoy!")
    else:
        print("Please enter a valid coffee type (espresso/latte/cappuccino).")

