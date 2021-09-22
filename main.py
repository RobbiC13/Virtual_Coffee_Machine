from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
# Turn off the coffee machine by entering "off" to the prompt
# Print report resources
# Check resources sufficient?
# Process coins
# Check transaction successful?
# Make coffee

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:  \n")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)

            # payment = process_coins()
            # if is_transaction_successful(payment, drink["cost"]):
                # make_coffee(order, drink["ingredients"])



