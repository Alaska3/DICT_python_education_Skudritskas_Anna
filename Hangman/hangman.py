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
    splitted_word = list(random.choice(word_list))
    guessed = ["-" for i in splitted_word]

    while constant > 0:
        print(' '.join(guessed))
        print("Attempts: ", constant)
        answer = input("Enter a latter: ").strip()
        if answer in guessed:
            constant -= 1
            print("No improvements")
        elif answer in splitted_word:
            for i, c in enumerate(splitted_word):
                if c == answer:
                    guessed[i] = answer
            if "-" not in guessed:
                print("You win")
                break
        else:
            print("That letter doesn't appear word")
            constant -= 1

        if constant == 0:
            print("You lost")





many()
guess()
