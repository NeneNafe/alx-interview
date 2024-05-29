#!/usr/bin/python3
""" Matrix function """


def rotate_2d_matrix(matrix):
    """ an n x n 2D matrix, rotate it 90 degrees clockwise """

    n = len(matrix[0])  # Determine size of matrix

    for i in range(n - 1, -1, -1):  # generates the seq in reverse
        for j in range(0, n):  # iterates through the columns
            matrix[j].append(matrix[i].pop(0))
