import random


def main():
    print("Enter the number of friends joining (including you): ")
    number = int(input())
    a = {}
    if number > 0:
        for i in range(number):
            print("Enter the name of every friend (including you), each on a new line: ")
            name = input()
            a[name] = 0
            print(a)
    else:
        print("No one is joining for the party.")

    print("Enter the total amount: ")
    bill = int(input())
    bill1 = round(bill / number, 2)
    for name in a:
        a[name] = bill1

    print(a)

    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No: ")
    user = input()
    if user == 'Yes':
        my_list = list(a.keys())
        r = random.choice(my_list)
        my_list1 = [r]
        new_d = dict.fromkeys(my_list1, 0)
        print(new_d)
        print(r, "is the lucky one!")
        number2 = number - 1
        bill2 = bill / number2
        for name in a:
            a[name] = bill2
        a.update(new_d)
        print(a)

    elif user == 'No':
        print("No one is going to be lucky.")
        print(a)
    else:
        print("Please, write Yes/No.")


if __name__ == "__main__":
    main()
