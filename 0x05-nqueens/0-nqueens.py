#!/usr/bin/python3
""" N_Queen """
import sys


def place_this(board, row, col):
    """ Places """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_with(board, row):
    """ Solves """
    n = len(board)
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if place_this(board, row, col):
            board[row] = col
            solve_with(board, row + 1)
            board[row] = -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_with(board, 0)
