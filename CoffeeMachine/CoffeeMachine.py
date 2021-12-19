# 1 stage
print("Starting to make a coffee.")
print("Grinding coffee beans.")
print("Boiling water.")
print("Mixing boiled water with crushed coffee beans.")
print("Pouring coffee into the cup.")
print("Pouring some milk into the cup.")
print("Coffee ready!")
# 2 stage
user = int(input("How many cups of coffee you need: "))
print("For", user, "cups of coffee you will need: ")
water = 200 * user
milk = 50 * user
coffee_beans = 15 * user
print(water, "ml of water")
print(milk, "ml of milk")
print(coffee_beans, "g of coffee beans")
