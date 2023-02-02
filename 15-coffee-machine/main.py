MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNY = 0.01

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

choice = ""
profit = 0


def machine_has_resources(coffee):
    # much better to do this with an ingredient dictionary elements loop for the specific coffee,
    # this way we don't have to even check if a key exists

    if resources['water'] - coffee['ingredients']['water'] >= 0\
            and resources['coffee'] - coffee['ingredients']['coffee']:
        resources['water'] -= coffee['ingredients']['water']
        resources['coffee'] -= coffee['ingredients']['coffee']
        if 'milk' in coffee['ingredients'].keys():
            if resources['milk'] - coffee['ingredients']['milk'] >= 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def print_report():
    # shortcut ALT + SHIFT and mouse drag to mark multiple lines at the same time
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${round(profit, 2)}")


while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    while choice != 'espresso' and choice != 'latte' and choice != 'cappuccino' and choice != 'off' and choice != 'report':
        choice = input("Try again - espresso/latte/cappuccino: ")

    if choice == 'off':
        print("Turning the machine off...")
    elif choice == 'report':
        print_report()
    else:
        # an admin choice can be made which has options like shut down, refuel, take money and so on. ^
        print(f"Your {choice} costs ${MENU[choice]['cost']}.")
        # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        print("Please insert coins: ")
        quarter_amount = int(input("How many quarters? "))
        dimes_amount = int(input("How many dimes? "))
        nickles_amount = int(input("How many nickles? "))
        pennies_amount = int(input("How many pennies? "))

        inserted_money = round(quarter_amount * 0.25 + dimes_amount * 0.10 + nickles_amount
                               * 0.05 + pennies_amount * 0.01, 2)
        print(f"You inserted a total of ${inserted_money}")

        if inserted_money >= MENU[choice]['cost']:
            if machine_has_resources(MENU[choice]):
                print(f"The machine returned ${round(inserted_money - MENU[choice]['cost'], 2)}")
                profit += MENU[choice]['cost']
                print(f"The machine made your {choice}. Enjoy!\n")
            else:
                print("Unfortunately the machine does not have enough resources to make your coffee.\n")
        else:
            print("Not enough money, the machine returned your coins.\n")

print("Hello admin, the machine has been turned off.")
