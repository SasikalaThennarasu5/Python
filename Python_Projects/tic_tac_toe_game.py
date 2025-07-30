
import random
from functools import wraps

def validate_move(func):
    @wraps(func)
    def wrapper(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
            return func(self, row, col)
        else:
            print("Invalid move. Try again.")
            return False
    return wrapper

class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    @validate_move
    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = self.board + list(zip(*self.board)) + [  # rows and cols
            [self.board[i][i] for i in range(3)],        # main diag
            [self.board[i][2 - i] for i in range(3)]      # anti diag
        ]
        for line in lines:
            if line.count(self.current_player) == 3:
                return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def get_empty_cells(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    yield (i, j)

    def play(self):
        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn")
            if self.current_player == "X":
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    continue
            else:
                row, col = random.choice(list(self.get_empty_cells()))
                print(f"Computer chooses: {row}, {col}")

            if self.make_move(row, col):
                if self.check_winner():
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    break
                elif self.is_draw():
                    self.display_board()
                    print("It's a draw!")
                    break
                self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
