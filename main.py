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

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

COINS = {
    "One Cent": 0.01,
    "Five Cents": 0.05,
    "One Dime": 0.10,
    "Quarter Dollar": 0.25,
    "Half Dollar": 0.50,
    "One Dollar": 1.00,
}


def inserted_coins():
    penny = int(input("How many pennies? ")) * COINS["One Cent"]
    nickel = int(input("How many nickles? ")) * COINS["Five Cents"]
    dime = int(input("How many dimes? ")) * COINS["One Dime"]
    quarter = int(input("How many quarters? ")) * COINS["Quarter Dollar"]
    half = int(input("How many halfs? ")) * COINS["Half Dollar"]
    dollar = int(input("How many dollars? ")) * COINS["One Dollar"]

    return penny + nickel + dime + quarter + half + dollar


def enough(drink):
    if MENU[drink]["ingredients"]["water"] > resources["Water"]:
        return "Sorry there is not enough water."
    elif MENU[drink]["ingredients"]["coffee"] > resources["Coffee"]:
        return "Sorry there is not enough coffee."
    elif MENU[drink] == "cappuccino" or drink == "latte":
        if MENU[drink]["ingredients"]["milk"] > resources["Milk"]:
            return "Sorry there is not enough milk."
        else:
            return True
    else:
        return True


money = 0.0
on = True

while on:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if option == "off":
        print("The system has been shut down. Thanks.")
        break

    elif option == "report":
        for item in resources:
            print(f"{item}: {resources[item]}", end="")
            if item == "Coffee":
                print("g")
            else:
                print("ml")
        print(f"Money: ${money:.2f}")

    elif option == "espresso" or option == "latte" or option == "cappuccino":
        if enough(option) is True:
            paid = inserted_coins()
            if paid < MENU[option]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = paid - MENU[option]["cost"]
                money += MENU[option]["cost"]
                resources["Water"] -= MENU[option]["ingredients"]["water"]
                resources["Coffee"] -= MENU[option]["ingredients"]["coffee"]
                if option == "latte" or option == "cappuccino":
                    resources["Milk"] -= MENU[option]["ingredients"]["milk"]
                print(f"Here is ${change:.2f} dollars in change.")
                print(f"Here is your {option}☕. Enjoy!")
        else:
            print(enough(option))


