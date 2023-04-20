from coffee_machine_art import logo
import os
from datetime import datetime


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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_is_sufficient(order_item):
    for item in order_item:
        if order_item[item] > resources[item]:
            print(f"sorry there is not sufficient {item}")
            return False
    return True


def process_coins():
    print("Please insert coins :")
    quarter = int(input("How many quarters? $ "))
    dimes = int(input("How many dimes? $ "))
    nickels = int(input("How many nickels? $ "))
    pennies = int(input("How many pennies? $ "))

    total = ((0.25 * quarter) + (0.10 * dimes) + (00.05 * nickels) + (0.01 * pennies))
    return total


def check_transaction(total, resource_cost):
    if total >= resource_cost:
        change = round(total - resource_cost, 2)
        print(f"Here is your change $ {change}")
        global money
        money += resource_cost
        return True
    else:
        print("Sorry that's not enough money. Money is refunded .")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    print("Thank You 🙏🙏")
    os.system('cls')


print(logo)
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}gm")
        print(f"Money:{money}")
    else:
        coffee_get = MENU[choice]
        if resources_is_sufficient(coffee_get["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, coffee_get["cost"]):
                make_coffee(choice, coffee_get["ingredients"])
