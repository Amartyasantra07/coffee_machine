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


def is_sufficinet(ingredients):
    is_enough= True
    for item in ingredients:
        if ingredients[item]>= resources[item]:
            print(f"Sorry there is not enough{item}")
            is_enough = False
    return is_enough

def coins():
    print("Please insert coins")
    total= int(input("How many quarters?:"))*0.25
    total+= int(input("How many dimes?:"))*0.1
    total+= int(input("How many nickeles?:"))*0.05
    total+= int(input("How many pennies?:"))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received>=drink_cost:
        change= round(money_received-drink_cost ,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+= drink_cost
        return True
    
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False    
    
def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item]-= ingredients[item]
    print(f"Here is your {drink_name}☕")
        
            
is_on= True
while is_on:
    choice =input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice =="report":
        print(f"Available water is:{resources['water']}ml")
        print(f"Available milk is:{resources['milk']}ml")
        print(f"Available coffee is:{resources['coffee']}gms")
        print(f"Money is:${profit}")
    else:
        drink =MENU[choice]
        if is_sufficinet(drink["ingredients"]):
            payments =coins()
            if is_transaction_successful(payments,drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                
                
            
            
                
           
        