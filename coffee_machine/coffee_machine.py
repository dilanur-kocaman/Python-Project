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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# coin operated
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.10
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def current_resource():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${profit}")

def check_resource(order_ingredients):
    """Returns True when order can be made, False are ingredients."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]: 
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough

def transaction(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")     
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required imgredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")

continues = True
while continues:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        continues = False
    elif choice == "report":
        current_resource()
    else:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





































