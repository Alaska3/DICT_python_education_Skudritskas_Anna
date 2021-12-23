def sample():
    print("Enter cells: ")
    b = input()
    print("---------")
    print("| " + b[0] + " " + b[1] + " " + b[2] + " |")
    print("| " + b[3] + " " + b[4] + " " + b[5] + " |")
    print("| " + b[6] + " " + b[7] + " " + b[8] + " |")
    print("---------")
    a = b.count('X')
    f = b.count('0')
    g = b.count('_')
    if abs(a-f) > 1:
        print("Impossible!")
    elif g:
        print("Game not finished!")
    else:
        print('Draw!')
    # когда выиграли и крестики и нолики i
        if b[0] == b[1] == b[2] and (b[3] == b[4] == b[5] or b[6] == b[7] == b[8]) or \
                b[0] == b[3] == b[6] and (b[1] == b[4] == b[7] or b[2] == b[5] == b[8]) or \
                b[3] == b[4] == b[5] and b[6] == b[7] == b[8] or \
                b[1] == b[4] == b[7] and b[2] == b[5] == b[8]:
            print("Impossible")
    # определение победившего игрока
        elif b[0] == b[1] == b[2] or b[0] == b[4] == b[8] or b[0] == b[3] == b[6]:
            print(b[0], "wins")
        elif b[1] == b[4] == b[7] or b[3] == b[4] == b[5]:
            print(b[4], "wins")
        elif b[6] == b[7] == b[8] or b[6] == b[4] == b[2]:
            print(b[6], "wins")
        elif b[2] == b[5] == b[8]:
            print(b[2], "wins")


sample()
