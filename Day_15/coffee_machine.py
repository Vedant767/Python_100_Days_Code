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

def print_report(resources, money):
    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nProfit: {money}")

def check_ingredients(type_of_coffee):
    check = ''
    if type_of_coffee == 'espresso':
        if resources["water"] < 50:
            check = 'water'
        elif resources['coffee'] < 18:
            check = 'coffee'
    
    if type_of_coffee == 'latte':
        if resources["water"] < 200:
            check = 'water'
        elif resources['coffee'] < 24:
            check = 'coffee'
        elif resources['milk'] < 150:
            check = 'milk'
    
    if type_of_coffee == 'cappuccino':
        if resources["water"] < 250:
            check = 'water'
        elif resources['coffee'] < 24:
            check = 'coffee'
        elif resources['milk'] < 100:
            check = 'milk'
    if check == '':
        check = True
    return check
    
def process_coins(quarters, dimes, nickles, pennies):
    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies


def make_coffee(coffee_type):
    check = check_ingredients(coffee_type)
    global profit
    if check == True:
        if coffee_type == 'espresso':
            resources['water'] -= 50
            resources["coffee"] -= 18
            profit += 1.5
        if coffee_type == 'latte':
            resources['water'] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24
            profit += 2.5
        if coffee_type == 'cappuccino':
            resources['water'] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24
            profit += 3.0
    else:
        print("Sorry there is not enough {check}.")

def accept_coins():
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))

    total = process_coins(quarters, dimes, nickles, pennies)
    return total

next_order = True

# print(MENU['latte']['cost'])

while next_order:
    customer_order = input('What would you like? (espresso/ latte/ cappuccino): ')

    if customer_order == 'report':
        print_report(resources, profit)
    elif customer_order == 'espresso' or customer_order == 'latte' or customer_order == 'cappuccino':
        if check_ingredients:
            coins = accept_coins()
            if coins >= MENU[customer_order]['cost']:
                make_coffee(customer_order)
                if coins > MENU[customer_order]['cost']:
                    coins -= MENU[customer_order]['cost']
                    print(f"Here is {round(coins, 2)} in change.")
                print(f"Here is your {customer_order}. Enjoy!.")
            else:
                print("Sorry that's not enough money. Money refunded. ")
    elif customer_order == 'off':
        next_order = False

