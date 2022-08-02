import data

def res_sufficient(order_ingridients):
    '''Checks if there is enough ingridients to make selected drink'''
    for item in order_ingridients:
        if order_ingridients[item] >= data.resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def count_coins():
    '''Returns the total calculated from inserted coins'''
    print("please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_success(money_recieved, drink_cost):
    '''Return true when the payment is accepted, or false if money is insufficient'''
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        if change > 0:
            print(f"here is your drink and ${change} in change. ")
        data.profit += drink_cost
        return True
    else:
        print("sorry, that's not enough money. money refunded")
        return False

is_on = True

while True:
    choice = input("what coffee would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Milk: {data.resources['milk']}")
        print(f"Water: {data.resources['water']}")
        print(f"Coffee: {data.resources['coffee']}")
        print(f"Money: ${data.profit}")
    else:
        drink = data.MENU[choice]
        cost = drink["cost"]
        print(f"You chose: {choice}, please insert ${cost}")
        if res_sufficient(drink["ingredients"]):
            money = count_coins()
            transaction_success(money, cost)


        