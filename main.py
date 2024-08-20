from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of MoneyMachine, CoffeeMaker, and Menu
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True

print("Welcome to Coffee Maker☕")
while is_on:
    # Get available menu items
    options = menu.get_items()
    # Ask user for their choice
    choice = input(f"What would you like? {options}").lower()
    if choice == "off":
        # Turn off the coffee machine
        is_on = False
    elif choice == "report":
        # Print report of coffee maker resources and money machine profit
        coffe_maker.report()
        money_machine.report()
    else:
        # Find the user's chosen drink
        drink = menu.find_drink(choice)
        # Check resources and process payment before making coffee
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)