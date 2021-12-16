import random


# 1 этап
def many():
    print("HANGMAN")
    print("The game will be soon")


word_list = ['python', 'java', 'javascript', 'php']  # 3 этап


# 2 этап
def guess():
    input("Press Enter to start the game: ")
    print("Guess the word: ")
    ans_robot = random.choice(word_list)
    print(ans_robot[0] + ans_robot[1] + ans_robot[2] + '-' * (len(ans_robot)-3))  # 4 этап
    ans = input()
    if ans == ans_robot:
        print("You survived!")
    else:
        print("You lost!")


many()
guess()
