import random


# 1 этап
def many():  #
    print("HANGMAN")
    print("The game will be soon")


word_list = ['python', 'java', 'javascript', 'php']  # 3 этап


# 2 этап
def guess():
    input("Press Enter to start the game: ")
    print("Guess the word: ")
# 5 этап
    constant = 8
    word = random.choice(word_list)
    splitted_word = list(word)
    guessed = ["-" for i in splitted_word]
    english_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'l', 'g', 'k', 'j', 'i', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while constant > 0:
        print(' '.join(guessed))
        print("Attempts: ", constant)
        answer = input("Enter a latter: ").strip()
        if answer not in english_letters:
            print("Please, enter a lowercase English letter")
            constant = constant
            continue
        elif len(answer) >= 2:
            print("You should input a single letter")
            constant = constant
            continue
        if answer in guessed:
            constant -= 1
            print("You've already guessed this letter")

        elif answer in splitted_word:
            for i, c in enumerate(splitted_word):
                if c == answer:
                    guessed[i] = answer
            if "-" not in guessed:
                print(word)
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear word")
            constant -= 1

        if constant == 0:
            print("You lost")





many()
guess()
