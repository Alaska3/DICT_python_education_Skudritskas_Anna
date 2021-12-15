# 1 этап
def hello():
    print("Hello! My name is Anny_robot.")
    print("I was created in 2021.")


# 2 этап
def name():
    a = input("Please, remind me your name. ")
    print("What a great name you have,", a)


# 3 этап
def your_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5, and 7. ")

    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())

    age = ((remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105)
    print("Your age is", age, ";", "that's good time to start programming!")


# 4 этап
def number():
    print("Now i will prove to you that I can count to any number you want.")
    for i in range(int(input()) + 1):
        print(str(i) + "!")
