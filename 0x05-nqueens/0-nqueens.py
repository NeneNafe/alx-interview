#!/usr/bin/python3
""" A function that solves the N queens puzzle """


import sys


def is_safe(board, row, col, Num):
    """Check if there is a queen in the same column

    Args:
        board: List of list with the length sys.argv[1]
        row: To check if is_safe doing a movement in this position
        col: To check if is_safe doing a movement in this position
        N: The size of the board
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, Num, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def PrintBoard(board):
    """ Prints the board """
    NewList = []
    for i, row in enumerate(board):
        value = []
        for j, col in enumerate(row):
            if col == 1:
                value.append(i)
                value.append(j)
        NewList.append(value)
    print(NewList)


def solveNqueens(board, col, num):
    """ Solves the numbers on a board with queens """

    if (col == num):
        PrintBoard(board)
        return True
    result = False
    for i in range(num):
        if (is_safe(board, i, col, num)):
            board[i][col] = 1

            result = solveNqueens(board, col + 1, num) or result
            board[i][col] = 0
    return result


def solve(num):
    """ Finds all the possibilities on the board """
    board = [[0 for i in range(num)]for i in range(num)]

    if not solveNqueens(board, 0, num):
        return False

    return True


def to_validate(args):
    """ Verify if the size to the answer is possible """
    if (len(args) == 2):
        try:
            num = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if num < 4:
            print("N must be at least 4")
            exit(1)
        return num
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    num = to_validate(sys.argv)
    solve(num)
