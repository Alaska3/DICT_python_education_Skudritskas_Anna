text = 0
text_1 = ""


def plain():
    global text_1
    text_1 += input("Text:> ")
    func()


def bold():
    global text, text_1
    text = input("Text:> ")
    text_1 = "**" + text + "**"
    func()


def italic():
    global text, text_1
    text = input("Text:> ")
    text_1 = "*" + text + "*"
    func()


def header():
    global text, text_1
    level = int(input('Level: > '))
    if level not in range(1, 7):
        print('The level should be within the range of 1 to 6. Try again')
        header()
    else:
        text = input('Text: > ')
        text_1 = '#' * level + ' ' + text + '\n'
        func()


def link():
    global text_1
    label = input('Label: > ')
    url = input('URL: > ')
    text_1 += '\n' + '[' + label + ']' + '(' + url + ')' + '\n'
    func()


def inline_code():
    global text_1
    b = input('Enter your text: > ')
    text_1 += '\n' + '~' + b + '~' + '\n'
    func()


def ordered_list():
    global text_1
    row = int(input("Number of rows:> "))
    if row > 0:
        for i in range(1, row + 1):
            a = str(input("Row #" + str(i) + ": >"))
            text_1 = (str(i) + "." + a)
    else:
        print("The number of rows should be greater than zero.")
        ordered_list()
    func()


def unordered_list():
    global text_1
    row = int(input("Number of rows:> "))
    if row > 0:
        for i in range(1, row + 1):
            a = str(input("Row #" + str(i) + ": >"))
            text_1 = ('*' + a + '\n')
    else:
        print("The number of rows should be greater than zero.")
        unordered_list()
    func()


def new_line():
    global text_1
    text_1 += "\n"
    func()


def helping():
    print("Available formatters: plain, bold, italic, header, link, inline-code, \
ordered-list, unordered-list, new-line")
    print("Special commands: help!, done!")
    func()


def done():
    file = open('output.md', 'w')
    file.write(text_1)
    file.close()


def func():
    print("Available formatters: plain, bold, italic, header, link, inline-code, \
ordered-list, unordered-list, new-line")
    print("Special commands: help!, done!")
    us_input = input("Chose a formatter: ")
    if us_input == "plain":
        plain()
    elif us_input == "bold":
        bold()
    elif us_input == "italic":
        italic()
    elif us_input == "header":
        header()
    elif us_input == "link":
        link()
    elif us_input == "inline-code":
        inline_code()
    elif us_input == "ordered-list":
        ordered_list()
    elif us_input == "unordered-list":
        unordered_list()
    elif us_input == "new-line":
        new_line()
    elif us_input == "help!":
        helping()
    elif us_input == "done!":
        done()
    else:
        print("Unknown formatting type or command.")
        func()


func()

