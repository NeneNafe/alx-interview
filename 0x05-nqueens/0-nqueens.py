#!/usr/bin/python3
""" A function that solves the N queens puzzle """


import sys


def is_safe(board, row, col):
    """Check if there is a queen in the same column

    Args:
        board: List of list with the length sys.argv[1]
        row: To check if is_safe doing a movement in this position
        col: To check if is_safe doing a movement in this position
        N: The size of the board
    """
    for i in range(row):
        if board[i] == col:
            return False
        if abs(row - i) == abs(board[i] - col):
            return False

    return True


def solveNqueens(num):
    def backtracking(row, board, results):
        """ Solves the numbers on a board with queens """
        if row == num:
            results.append(board[:])
        for col in range(num):
            if is_safe(board=board, row=row, col=col):
                board[row] = col
                backtracking(board=board, row=row + 1, results=results)
                board[row] = -1
    results = []
    board = [-1] * num
    backtracking(row=0, board=board, results=results)
    return results


def to_validate():
    """ Verify if the size to the answer is possible """
    if (len(sys.argv) != 2):
        print("N must be a number")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        if num < 4:
            print("N must be at least 4")
            sys.exit(1)
        return num
    except ValueError:
        print("N must be a number")
        sys.exit(1)


def main():
    """ the main function
    """
    num = to_validate()
    results = solveNqueens(num)
    for result in results:
        outcome = [[rows, column] for rows, column in enumerate(result)]
        print(outcome)


if __name__ == "__main__":
    main()
