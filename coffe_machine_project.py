# Define the MENU dictionary with available drinks, their ingredients, and costs.
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

# Initialize profit and resources variables.
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True if the order can be made, and False if resources are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coin():
    """Returns the total amount of money calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_sucessful(money_received, drink_cost):
    """Returns True if the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money has been refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources and serves the drink."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

# Main program loop
print("Welcome to the Coffee Machine ☕")

is_on = True
while is_on:
    # Ask the user what they would like to order.
    choice = input(
        "What would you like? (espresso☕, latte☕, cappuccino☕)\n"
    ).lower()
    
    # Option to turn off the machine.
    if choice == "off":
        is_on = False
    
    # Option to print a report of current resources and profit.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    
    # Process the user's drink choice.
    else:
        drink = MENU[choice]
        
        # Check if there are enough resources to make the drink.
        if is_resource_sufficient(drink["ingredients"]):
            # Process payment.
            payment = process_coin()
            
            # Check if the transaction is successful.
            if is_transaction_sucessful(payment, drink["cost"]):
                # Make the coffee if everything is successful.
                make_coffee(choice, drink["ingredients"])