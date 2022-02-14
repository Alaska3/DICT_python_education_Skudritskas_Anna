from random import *
num1 = randint(2, 9)
num2 = randint(2, 9)
my_list = [str(num1) + '*' + str(num2), str(num1) + '-' + str(num2), str(num1) + '+' + str(num2)]
rand = choice(my_list)
t = eval(rand)   # результат выполнения строки
print(rand)
user = int(input())

if user == t:
    print("Right!")
else:
    print("Wrong!")
