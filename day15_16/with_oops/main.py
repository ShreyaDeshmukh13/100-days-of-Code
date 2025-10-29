from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Coffee Makers . Here's Today's Menu : ")
money_machine = MoneyMachine()
coffee_maker =  CoffeeMaker()
is_on = True
menu =  Menu()

while is_on :
    option = menu.get_items()
    choice = input(f"What would you like?({option})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink)) and  money_machine.make_payment(drink.cost) :
            coffee_maker.make_coffee(drink)