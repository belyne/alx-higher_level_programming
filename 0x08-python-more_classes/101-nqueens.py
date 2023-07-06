#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(N):
    # Solve the N-Queens problem using backtracking

    def backtrack(board, col, N, solutions):
        if col >= N:
            # All queens have been placed, add solution to the list
            queens = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 1:
                        queens.append([row, col])
            solutions.append(queens)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                # Place a queen at board[row][col]
                board[row][col] = 1

                # Recur for the next column
                backtrack(board, col + 1, N, solutions)

                # Backtrack and remove the queen from board[row][col]
                board[row][col] = 0

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    backtrack(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
