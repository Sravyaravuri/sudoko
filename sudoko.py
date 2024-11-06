import random

def generate_sudoku(size=9):
    def pattern(r, c): return (size // 3 * (r % 3) + r // 3 + c) % size
    def shuffle(s): return random.sample(s, len(s))

    rows = [g * 3 + r for g in shuffle(range(3)) for r in shuffle(range(3))]
    cols = [g * 3 + c for g in shuffle(range(3)) for c in shuffle(range(3))]
    nums = shuffle(range(1, size + 1))

    # Create a full Sudoku grid
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # Remove some elements to create a puzzle
    squares = size * size
    empties = squares * 3 // 4
    for _ in range(empties):
        x, y = divmod(random.randrange(squares), size)
        board[x][y] = 0

    return board

# Print the board for visualization
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Generate and display a puzzle
sudoku_board = generate_sudoku()
print_board(sudoku_board)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def play_sudoku(board):
    print("Welcome to Sudoku!")
    print_board(board)

    while True:
        row, col, num = map(int, input("Enter row, column, and number (e.g., 1 2 3) or -1 to quit: ").split())
        if row == -1:
            print("Exiting the game.")
            break

        row, col = row - 1, col - 1
        if is_valid(board, row, col, num) and board[row][col] == 0:
            board[row][col] = num
            print_board(board)

            if all(all(cell != 0 for cell in row) for row in board):
                print("Congratulations! You've completed the Sudoku puzzle.")
                break
        else:
            print("Invalid move. Try again.")

# Make a copy of the puzzle so that the original remains unsolved
import copy
puzzle_board = copy.deepcopy(sudoku_board)

# Play the game
play_sudoku(puzzle_board)
