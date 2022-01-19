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
