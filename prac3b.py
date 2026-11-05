#TC: n!
# 8 Queens Problem using Backtracking
N = 8
board = [['.' for _ in range(N)] for _ in range(N)]
# Check whether a queen can be placed
def safe(row, col):

    for i in range(row):
        # Check column and diagonals
        dig1 = col - (row - i)
        dig2 = col + (row - i)
        if (board[i][col] == 'Q' or
            (dig1 >= 0 and
             board[i][dig1] == 'Q') or
            (dig2 < N and
             board[i][dig2] == 'Q')):

            return False

    return True


# Backtracking function
def solve(row):
    if row == N:
        return True

    for col in range(N):

        if safe(row, col):

            board[row][col] = 'Q'

            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = '.'

    return False
# Execute program
print("Starting Board:")
for row in board:
  print(' '.join(row))
if solve(0):
    print("Solution to 8 Queens Problem:\n")

    for row in board:
        print(' '.join(row))

else:
    print("No solution exists")
