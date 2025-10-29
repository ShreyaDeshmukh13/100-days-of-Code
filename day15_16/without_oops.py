MENU = {
    "espresso" : {
        "ingredients": {
            "water" : 50 ,
            "coffee" : 18 ,
        } ,
        "cost" : 15 ,
    },
    "latte" : {
        "ingredients": {
            "water" : 200 ,
            "milk" : 150 ,
            "coffee" : 24 ,
        },
        "cost" : 25 ,
    },
    "cappuccino" : {
        "ingredients": {
            "water" : 250 ,
            "milk" : 100 ,
            "coffee" : 24 ,
        },
        "cost" : 35 ,
    }
}

profit = 0

resources = {
   "water" : 300 ,
    "milk" : 200 ,
    "coffee" : 100 ,
}

def is_resource_sufficient(order_ingredients):
    """"Returns True if the order can be made and false if ingredients are not sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please Insert coins .")
    total = int(input("How many one rupee coins ? : ")) * 1
    total += int(input("How many five rupee coins ? : ")) * 5
    total += int(input("How many ten rupee coins ? : ")) * 10
    total += int(input("How many twenty rupee coins ? : ")) * 20
    return total

def is_transaction_successful (money_received , drink_cost):
    """Returns True when the payment is accepted , or False if money is insufficient ."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here's {change} rupee coins in change.")
        global profit
        profit += drink_cost
        return True
    else :
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name , order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕:)")


is_on = True
while is_on :
    choice = input (" What Would you like? (espresso/latte/cappuccino):")
    if choice == "off" :
        is_on = False
    elif choice == "report" :
        print(f"Water : {resources["water"]} ml")
        print(f"Milk : {resources["milk"]} ml")
        print(f"Coffee: {resources["coffee"]} g")
        print(f"Money : {profit} rupees")

    else :
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice , drink["ingredients"])