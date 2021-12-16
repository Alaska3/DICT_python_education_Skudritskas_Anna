# 1 этап
def many():
    print("HANGMAN")
    print("The game will be soon")


# 2 этап
def guess():
    input("Press Enter to start the game: ")
    print("Guess the word: ")
    ans = input()

    if ans == "python":
        print("You survived!")
    else:
        print("You lost!")


many()
guess()
