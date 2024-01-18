MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
def sufficient_resources(user_input):
    for key in resources:
        if resources[key] <= MENU[user_input]["ingredients"][key]:
            print(f"There is not enough {key}")
            return False
        else:
            return True

def calculate_money():
    q = int(input("How many Quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickles?"))
    p = int(input("How many pennies?"))
    return q*.25 + d*.10 + n*.05 + p*.01

def resources_left(user_input):
    for key in resources:
        resources[key] = resources[key] - MENU[user_input]["ingredients"][key]



def is_transaction_possible(payment,user_input):
    if payment >= MENU[user_input]["cost"]:
        change = round(payment - MENU[user_input]["cost"],2)
        print(f"Here is your change {change}")
        global profit
        profit += MENU[user_input]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        is_on = False

    elif user_input == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']}76g")
        print(f"Money: ${profit}")
    else:
        if sufficient_resources(user_input):
            payment = calculate_money()
            updated = is_transaction_possible(payment,user_input)
            if updated == True:
                resources_left(user_input)














