class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.coffee_beans = 120
        self.milk = 540
        self.money = 550
        self.cups = 9

    def print_state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(f"$ {self.money} of money")

    def select_action(self):
        while True:
            print("ATTENTION!!! Here you must write words no numbers!")
            user_input = input('Write action:\n 1-buy\n 2-fill\n 3-take\n 4-remaining\n 5-exit\n: ')
            if user_input == "buy":
                CoffeeMachine.buy(self)
            elif user_input == "fill":
                CoffeeMachine.fill(self)
            elif user_input == "take":
                CoffeeMachine.take(self)
            elif user_input == "remaining":
                CoffeeMachine.print_state(self)
            elif user_input == "exit":
                break
            else:
                print("invalid choice")

    def choose_coffee(self):
        print()
        move = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' 4 - back to main menu: ')
        if move == '4':
            return 0
        return int(move)

    def numbers(self, needed_water, needed_milk, needed_coffee):
        if self.water < needed_water:
            print('Sorry, not enough water!')
            return False
        if self.milk < needed_milk:
            print('Sorry, not enough milk!')
            return False
        if self.coffee_beans < needed_coffee:
            print('Sorry, not enough coffee_beans!')
            return False
        if self.cups < 1:
            print('Sorry, not enough cups!\n')
            return False
        print('I have enough resources, making you a coffee!\n')
        return True

    def buy(self):
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        if user_input == '1':
            if CoffeeMachine.numbers(self, 250, 0, 16):
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.cups -= 1
        elif user_input == '2':
            if CoffeeMachine.numbers(self, 350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.cups -= 1
        elif user_input == '3':
            if CoffeeMachine.numbers(self, 200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.cups -= 1
        elif user_input == "back":
            return
        else:
            print('invalid choice')
            return CoffeeMachine.buy(self)

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.coffee_beans += int(input('Write how many grams of coffee coffee_beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))

    def take(self):
        print(f'I gave you {self.money}')
        self.money = 0


if __name__ == "__main__":
    coffee = CoffeeMachine()
    coffee.select_action()
