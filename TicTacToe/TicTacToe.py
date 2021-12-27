import random


def edit_user_turn(user):             # поменять X на 0
    return 'X' if user == 'O' else 'O'


def first_user():
    return random.randint(0, 1)


class TicTacToe:

    def __init__(self):
        self.grid = []

    def create_grid(self):
        for i in range(3):   # диапазон от 0 до 3
            row = []
            for j in range(3):
                row.append('-')
            self.grid.append(row)

    def spot(self, row, col, user):   # исправили место
        self.grid[row][col] = user

    def if_win(self, user):
        win = False
        c = len(self.grid)
        # выигрыш по вертикали
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] == user:
                win = True
        # выигрыш по горизонтали
        for row in range(c):
            if self.grid[row][0] == self.grid[row][1] == self.grid[row][2] == user:
                win = True
        # выигрыш по диагонали 1
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == user:
            win = True
        # выигрыш по диагонали 2
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == user:
            win = True

        return win

    def is_grid_filled(self):  # если заполнен ряд
        full = True
        for row in self.grid:
            for item in row:
                if item == '-':
                    full = False

        return full

    def is_cell_filled(self, row, col):  # если заполена ячейка
        full = False
        if self.grid[row][col] != '-':
            full = True
        return full

    def show_grid(self):
        for row in self.grid:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_grid()
        count = 0
        user = 'O' if first_user() == 1 else 'X'
        self.show_grid()

        while True:
            print(f"Player {user} turn")

            row, col = list(
                map(int, input("Enter cells: ").split()))
            print()

            if not self.is_cell_filled(row - 1, col - 1):
                self.spot(row - 1, col - 1, user)
                count += 1
                self.show_grid()
                if self.if_win(user):
                    print(f"Player {user} wins the game!")
                    break

                if self.is_grid_filled():
                    print("Draw!")
                    break
                user = edit_user_turn(user)
            else:
                print("That place is already filled.")
                continue

        print()


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
