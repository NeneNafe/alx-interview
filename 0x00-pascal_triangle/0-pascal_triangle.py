#!/usr/bin/python3

"""A function that returns a list of lists of integers
    representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """function prototype
    Args:
        n which is an integer_
    """
    if (n <= 0):
        return []

    triangle = []
    for rownum in range(n):
        newValue = 1
        printlist = [newValue]
        for iteration in range(rownum):
            newValue = newValue * (rownum - iteration) * 1 / (iteration + 1)
            printlist.append(int(newValue))
        triangle.append(printlist)
    return triangle
    
