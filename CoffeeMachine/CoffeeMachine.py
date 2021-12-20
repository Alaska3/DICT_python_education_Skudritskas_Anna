print("Starting to make a coffee.")
print("Grinding coffee beans.")
print("Boiling water.")
print("Mixing boiled water with crushed coffee beans.")
print("Pouring coffee into the cup.")
print("Pouring some milk into the cup.")
print("Coffee ready!")

# 5 stage
money = 550
water = 400
milk = 540
coffee_beans = 120
cups = 9


def remaining():
    print("The coffee machine has: ")
    print(str(water), "of water")
    print(str(coffee_beans), "of coffee beans")
    print(str(cups), "of disposable caps")
    print(str(money), "of money")


def number():
    if water < 0:
        print("Not enough water.")
        return False
    elif milk < 0:
        print("Not enough milk.")
        return False
    elif coffee_beans < 0:
        print("Not enough coffee beans.")
        return False
    elif cups < 0:
        print("Not enough caps.")
        return False
    elif money < 0:
        print("Not enough money.")
        return False
    else:
        return True


def buy():
    global water, coffee_beans, milk, cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    user_input = input()
    if int(user_input) == 1:
        if number():
            water -= 250
            coffee_beans -= 16
            cups -= 1
            money += 4
            print("I have enough resources making you a espresso.")
    elif int(user_input) == 2:
        if number():
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 7
            print("I have enough resources making you a latte.")
    elif int(user_input) == 3:
        if number():
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 6
            print("I have enough resources making you a cappuccino.")


def fill():
    global water, milk, coffee_beans, cups
    print("How many ml of water to add to the coffee machine?")
    water_add = int(input())
    water += water_add
    print("How many ml of milk to add to the coffee machine?")
    milk_add = int(input())
    milk += milk_add
    print("How many cup to add to the coffee machine?")
    cups_add = int(input())
    cups = cups_add
    print("How many grams of coffee beans to add to the coffee machine?")
    beans_add = int(input())
    coffee_beans += beans_add


def take():
    global money
    print("I gave you", str(money), "\n")
    money = 0


def option():
    while True:
        remaining()
        print("Please, choose options: 'buy', 'fill', 'take', 'remaining'")
        user_input = input()
        if user_input == 'buy':
            buy()
        elif user_input == 'fill':
            fill()
        elif user_input == 'take':
            take()
        elif user_input == 'remaining':
            remaining()

        print("What ou want to do next: 'back', 'exit'")
        user_next_input = input()
        if user_next_input == 'back':
            continue
        elif user_next_input == 'exit':
            break


option()
