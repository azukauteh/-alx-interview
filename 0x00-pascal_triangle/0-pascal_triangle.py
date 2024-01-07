#!/usr/bin/python3
'''Module to return pascal triangle'''


def pascal_triangle(n):
    """ Check if n is not a positive integer"""
    if n <= 0 or not isinstance(n, int):
        return []

    """ Initialize Pascal's Triangle with the first row"""
    triangle = [[1]]

    for i in range(1, n):
        """ Calculate the next row based on the previous row"""
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)

        """ Add the current row to Pascal's Triangle"""
        triangle.append(row)

    return triangle
