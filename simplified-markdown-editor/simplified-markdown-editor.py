text = 0
text_1 = ""


def func():
    us_input = ''
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
        pass
    else:
        print("Unknown formatting type or command.")
        us_input = input("Chose a formatter: ")


def plain():
    global text_1
    text_1 += input("Text:> ")


def bold():
    global text, text_1
    text = input("Text:> ")
    text_1 = "**" + text + "**"


def italic():
    global text, text_1
    text = input("Text:> ")
    text_1 = "*" + text + "*"


def header():
    global text, text_1
    level = int(input('Level: > '))
    if level not in range(1, 7):
        print('The level should be within the range of 1 to 6. Try again')
        header()
    else:
        text = input('Text: > ')
        text_1 = '#' * level + ' ' + text + '\n'


def link():
    global text_1
    label = input('Label: > ')
    url = input('URL: > ')
    text_1 += '\n' + '[' + label + ']' + '(' + url + ')' + '\n'


def inline_code():
    pass


def ordered_list():
    pass


def unordered_list():
    pass


def new_line():
    global text_1
    text_1 += "\n"


def helping():
    print("Available formatters: plain, bold, italic, header, link, inline-code, \
    ordered-list, unordered-list, new-line")
    print("Special commands: help!, done!")
    func()




func()

