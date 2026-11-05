#TC:9^m
def valid(board, row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def display():
  for row in board:
    print(' '.join(str(n) if n != 0 else '.' for n in row))
        
def solve(board):
    # Find an empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:

                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if valid(board, i, j, num):
                        board[i][j] = num

                        if solve(board):
                            return True

                        # Backtrack
                        board[i][j] = 0

                return False

    return True


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("SUDOKU SOLVER")
print("-------------------------")
print("Initial Sudoku:")

display()
if solve(board):
    print("\nSolved Sudoku:")
    display()
else:
    print("No solution exists")
