from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# ^ these files were provided by the lecturer, we adapt them to work together

MENU = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_off = False
action_choice = ""

while not is_machine_off:
    action_choice = input(f"Select drink: {MENU.get_items()} ")
    coffee_ordered = MENU.find_drink(action_choice)
    while coffee_ordered is None \
            and action_choice != "report" and action_choice != "off":
        action_choice = input(f"Try again: {MENU.get_items()} ")

    if action_choice == "off":
        is_machine_off = True
    elif action_choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        if coffee_machine.is_resource_sufficient(coffee_ordered):
            if money_machine.make_payment(coffee_ordered.cost):
                coffee_machine.make_coffee(coffee_ordered)
