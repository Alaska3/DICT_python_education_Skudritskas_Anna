from random import *
print("Which level do you want? Enter a number: ")
print("1 - simple operations with numbers 2-9")
print("2 - integral squares of 11-29")
us = input()


def level1():
    if us == '1':
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
        print("Your mark", n, "/ 5. Would you like save the result to the file? Enter yes or no.")
        us1 = input()
        if us1 == 'yes' or 'YES' or 'y' or 'Yes' and not 'no':
            print('What\'s your name?')
            name = input()
            new_file = open('results.txt', '+w')
            new_file.write(name)
            new_file.write(': ')
            new_file.write(str(n))
            new_file.write('/5 in level 1 (simple operations with numbers 2-9)')
            new_file.close()
            print('The results are saved in "results.txt".')
        else:
            print()


def level2():
    if us == '2':
        i = 0
        n = 0
        while i < 5:
            i += 1
            num1 = randint(11, 29)
            num2 = 2
            a = num1 ** num2
            print(f'{num1} ** {num2}')
            response = input()
            if not response:
                print('Incorrect format!')
                i -= 1
                continue
            try:
                ans = int(response)
                if ans == a:
                    print('Right!')
                    n += 1
                else:
                    print('Wrong!')
            except ValueError:
                print('Incorrect format!')
                i -= 1
        print("Your mark", n, "/ 5. Would you like save the result to the file? Enter yes or no.")
        us1 = input()
        if us1 != 'yes' and 'YES' and 'y' and 'Yes':
            print('What\'s your name?')
            name = input()
            new_file = open('results.txt', '+w')
            new_file.write(name)
            new_file.write(': ')
            new_file.write(str(n))
            new_file.write('/5 in level 2 (integral squares of 11-29)')
            new_file.close()
            print('The results are saved in "results.txt".')
        else:
            print()


level1()
level2()
