from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

is_machine_on = True

while is_machine_on:
    choice = input(f"What would you like? ({menu_obj.get_items()}): ").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
       drink = menu_obj.find_drink(choice)
       if drink is not None:
           if coffee_maker_obj.is_resource_sufficient(drink):
               if money_machine_obj.make_payment(drink.cost):
                   coffee_maker_obj.make_coffee(drink)