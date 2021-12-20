print("Starting to make a coffee.")
print("Grinding coffee beans.")
print("Boiling water.")
print("Mixing boiled water with crushed coffee beans.")
print("Pouring coffee into the cup.")
print("Pouring some milk into the cup.")
print("Coffee ready!")

# 4 stage
money = 550
water = 400
milk = 540
coffee_beans = 120
caps = 9


def include():
    print("The coffee machine has: ")
    print(str(water), "of water")
    print(str(coffee_beans), "of coffee beans")
    print(str(caps), "of disposable caps")
    print(str(money), "of money")


print()


def buy():
    global water
    global coffee_beans
    global milk
    global money
    print("Please, select the type of coffee: 1 - espresso, 2 - latte, 3 - cappuccino")
    user = int(input())
    if user == 1:
        water -= 250
        coffee_beans -= 16
        money -= 4
    elif user == 2:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
    elif user == 3:
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 6


print()


def fill():
    global water
    global milk
    global coffee_beans
    print("How many ml of water to add to the coffee machine?")
    water_add = int(input())
    water += water_add
    print("How many ml of milk to add to the coffee machine?")
    milk_add = int(input())
    milk += milk_add
    print("How many grams of coffee beans to add to the coffee machine?")
    beans_add = int(input())
    coffee_beans += beans_add


print()


def take():
    global money
    print("I gave you", str(money), "/n")
    money = 0


print()


def option():
    include()
    print("Please, choose options: 'buy', 'fill', 'take' ")
    user = input()
    if user == 'buy':
        buy()
        include()
    elif user == 'fill':
        fill()
        include()
    elif user == 'take':
        take()
        include()


option()
