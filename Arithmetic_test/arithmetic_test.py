from random import *
from math import *
print('Which level do you want? Enter a number: ')
print('1 - simple operations with numbers 2-9')
print('2 - integral squares of 11-29')
print('3 - remainder of the division')
print('4 - cube root of 1-20')
print('5 - factorial of 1-10')
us = input()


def level1():
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
            print('Incorrect format!')
            print(f'{rand}')
            ans1 = int(input())
            if ans1 == t:
                print('Right!')
                n += 1
            else:
                print('Wrong!')
            continue
        try:
            ans = int(user)
            if ans == t:
                n += 1
                print('Right')
            else:
                print('Wrong')
        except ValueError:
            print('Incorrect format!')
            print(f'{rand}')
            ans2 = int(input())
            if ans2 == t:
                print('Right!')
                n += 1
            else:
                print('Wrong!')

    print('Your mark', n, '/ 5. Would you like save the result to the file? Enter yes or no.')
    us1 = input()
    if us1 in ('yes', 'YES', 'y', 'Yes'):
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
    if n < 3:
        print('Not enough points to pass to the next level. Try again! ')
        print('Do you want complete the level again?')
        user_level1 = input()
        if user_level1 in ('yes', 'y', 'YES', 'Yes'):
            level1()
    elif n > 3:
        print('Do you want to go to the next level?')
        user_level = input()
        if user_level in ('yes', 'y', 'YES', 'Yes'):
            level2()
        else:
            print()
    else:
        print()


def level2():
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
            print(f'{num1} ** {num2}')
            ans6 = int(input())
            if ans6 == a:
                print('Right!')
                n += 1
            else:
                print('Wrong!')
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
            print(f'{num1} ** {num2}')
            ans9 = int(input())
            if ans9 == a:
                print('Right!')
                n += 1
            else:
                print('Wrong!')

    print('Your mark', n, '/ 5. Would you like save the result to the file? Enter yes or no.')
    us1 = input()
    if us1 in ('yes', 'y', 'YES', 'Yes'):
        print('What\'s your name?')
        name = input()
        new_file = open('results.txt', 'a')
        new_file.write('\n')
        new_file.write(name)
        new_file.write(': ')
        new_file.write(str(n))
        new_file.write('/5 in level 2 (integral squares of 11-29)')
        new_file.close()
        print('The results are saved in "results.txt".')
    else:
        print()
    if n < 3:
        print('Not enough points to pass to the next level. Try again! ')
        print('Do you want complete the level again?')
        user_level2 = input()
        if user_level2 in ('yes', 'y', 'YES', 'Yes'):
            level2()
    elif n > 3:
        print('Do you want to go to the next level?')
        user_level = input()
        if user_level in ('yes', 'y', 'YES', 'Yes'):
            level3()
        else:
            print()
    else:
        print()


def level3():
    i = 0
    n = 0
    while i < 5:
        i += 1
        num1 = randint(1, 1000)
        num2 = randint(1, 1000)
        a = num1 % num2
        print(f'{num1} % {num2}')
        response = input()
        if not response:
            print('Incorrect format!')
            print(f'{num1} % {num2}')
            ans4 = int(input())
            if ans4 == a:
                print('Right!')
                n += 1
            else:
                print('Wrong!')
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
            print(f'{num1} % {num2}')
            ans1 = int(input())
            if ans1 == a:
                print('Right!')
                n += 1
            else:
                print('Wrong!')

    print('Your mark', n, '/ 5. Would you like save the result to the file? Enter yes or no.')
    us1 = input()
    if us1 in ('yes', 'y', 'YES', 'Yes'):
        print('What\'s your name?')
        name = input()
        new_file = open('results.txt', 'a')
        new_file.write('\n')
        new_file.write(name)
        new_file.write(': ')
        new_file.write(str(n))
        new_file.write('/5 in level 3 (remainder of the division)')
        new_file.close()
        print('The results are saved in "results.txt".')
    else:
        print()
    if n < 3:
        print('Not enough points to pass to the next level. Try again! ')
        print('Do you want complete the level again?')
        user_level3 = input()
        if user_level3 in ('yes', 'y', 'YES', 'Yes'):
            level3()
    elif n > 3:
        print('Do you want to go to the next level?')
        user_level = input()
        if user_level in ('yes', 'y', 'YES', 'Yes'):
            level4()
        else:
            print()
    else:
        print()


def level4():
    i = 0
    n = 0
    while i < 5:
        i += 1
        lst = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]
        num = choice(lst)
        a = ceil(num ** (1 / 3))
        print(f'∛{num}')
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
            print(f'∛{num}')
            ans1 = int(input())
            if ans1 == a:
                print('Right!')
                n += 1
            else:
                print('Wrong!')

    print('Your mark', n, '/ 5. Would you like save the result to the file? Enter yes or no.')
    us1 = input()
    if us1 in ('Yes', 'y', 'YES', 'yes'):
        print('What\'s your name?')
        name = input()
        new_file = open('results.txt', 'a')
        new_file.write('\n')
        new_file.write(name)
        new_file.write(': ')
        new_file.write(str(n))
        new_file.write('/5 in level 4 (cube root of 1-20)')
        new_file.close()
        print('The results are saved in "results.txt".')
    else:
        print()
    if n < 3:
        print('Not enough points to pass to the next level. Try again! ')
        print('Do you want complete the level again?')
        user_level4 = input()
        if user_level4 in ('yes', 'y', 'YES', 'Yes'):
            level4()
    elif n >= 3:
        print('Do you want to go to the next level?')
        user_level = input()
        if user_level in ('yes', 'YES', 'y', 'Yes'):
            level5()
        else:
            print()
    else:
        print()


def level5():
    i = 0
    n = 0
    while i < 5:
        i += 1
        num = randint(1, 10)
        a = factorial(num)
        print(f'{num}!')
        response = input()
        if not response:
            print('Incorrect format!')
            print(f'{num}!')
            ans2 = int(input())
            if ans2 == a:
                print('Right!')
                n += 1
            else:
                print('Wrong!')
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
            print(f'{num}!')
            ans1 = int(input())
            if ans1 == a:
                print('Right!')
                n += 1
            else:
                print('Wrong!')

    print('Your mark', n, '/ 5. Would you like save the result to the file? Enter yes or no.')
    us1 = input()
    if us1 in ('yes', 'y', 'YES', 'Yes'):
        print('What\'s your name?')
        name = input()
        new_file = open('results.txt', 'a')
        new_file.write('\n')
        new_file.write(name)
        new_file.write(': ')
        new_file.write(str(n))
        new_file.write('/5 in level 5 (factorial of 1-10)')
        new_file.close()
        print('The results are saved in "results.txt".')
    else:
        print()
    if n < 3:
        print('Not enough points to pass to the next level. Try again! ')
        print('Do you want complete the level again?')
        user_level5 = input()
        if user_level5 in ('yes', 'y', 'YES', 'Yes'):
            level5()
        else:
            print()
    elif n >= 3:
        print('My congratulations! You completed all levels!!')
        user = input('Do you want to play the game again?')
        if user in ('yes', 'y', 'YES', 'Yes'):
            level1()
        else:
            print()
    else:
        print()


if us == '1':
    level1()
elif us == '2':
    level2()
elif us == '3':
    level3()
elif us == '4':
    level4()
elif us == '5':
    level5()
else:
    print('Incorrect format!')
