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

    while True:
        print(' '.join(guessed))
        print("Attempts: ", constant)
        answer = input("Enter a latter: ").strip()
        if answer in splitted_word:
            for i, c in enumerate(splitted_word):
                if c == answer:
                    guessed[i] = answer
        if answer == splitted_word:
            print("You survived!")
            break
        else:
            constant -= 1
        if constant == 0: 
            print("You lost!")
            break


many()
guess()
