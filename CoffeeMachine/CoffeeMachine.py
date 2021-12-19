# 1 stage
print("Starting to make a coffee.")
print("Grinding coffee beans.")
print("Boiling water.")
print("Mixing boiled water with crushed coffee beans.")
print("Pouring coffee into the cup.")
print("Pouring some milk into the cup.")
print("Coffee ready!")
# 3 stage
water = 200
milk = 50
coffee_beans = 15
print("Write how many ml of water the coffee machine has: ")
a = int(input())
print("Write, how many ml of milk the coffee machine has:")
b = int(input())
print("Write, how many grams of coffee beans the coffee machine has: ")
c = int(input())
print("Write, how many cups of coffee you will need: ")
coffee_cups = int(input())
water1 = a // water
milk1 = b // milk
coffee_beans1 = c // coffee_beans
number_cups = min([water1, milk1, coffee_beans1])
d = number_cups - coffee_cups
if coffee_cups == number_cups:
    print("Yes, I can make that amount of coffee.")
elif coffee_cups < number_cups:
    print("Yes, I can make that amount of coffee(and even", d, "more than that).")
else:
    print("No, I can make only", number_cups, "cups of coffee")
