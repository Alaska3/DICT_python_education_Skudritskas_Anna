from random import *
i = 0
n = 0
while i < 5:
    i += 1
    num1 = randint(2, 9)
    num2 = randint(2, 9)
    my_list = [str(num1) + '*' + str(num2), str(num1) + '-' + str(num2), str(num1) + '+' + str(num2)]
    rand = choice(my_list)
    t = eval(rand)  # результат выполнения строки
    print(rand)
    user = input()
    if not user:
        print("Incorrect format!")
        i -= 1
        continue
    try:
        ans = int(user)
        if ans == t:
            n += 1
            print('Right')
        else:
            print('Wrong')
    except ValueError:
        print("Incorrect format!")
        i -= 1
print("Your mark", n, "/ 5")
