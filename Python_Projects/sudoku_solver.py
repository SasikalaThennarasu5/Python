
import csv
from typing import List, Optional
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper

class Sudoku:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

    def is_valid(self, row: int, col: int, num: int) -> bool:
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def find_empty(self) -> Optional[tuple]:
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def possible_numbers(self, row: int, col: int):
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                yield num

    @timeit
    def solve(self) -> bool:
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty
        for num in self.possible_numbers(row, col):
            self.grid[row][col] = num
            if self.solve():
                return True
            self.grid[row][col] = 0
        return False

def load_sudoku_from_csv(file_path: str) -> List[List[int]]:
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            return [[int(num) for num in row] for row in reader]
    except Exception as e:
        print(f"Error loading file: {e}")
        return [[0]*9 for _ in range(9)]

if __name__ == "__main__":
    path = "sudoku_puzzle.csv"  # Replace with actual CSV path
    grid = load_sudoku_from_csv(path)
    game = Sudoku(grid)
    print("Initial Sudoku Grid:")
    game.print_grid()
    if game.solve():
        print("\nSolved Sudoku Grid:")
        game.print_grid()
    else:
        print("No solution exists.")
