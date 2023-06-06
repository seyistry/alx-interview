#!/usr/bin/python3
"""Rotate 2D Matrix
    """

# result = []


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
        matrix (list): n x n matrix
    """
    result = [i[:] for i in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sub = len(matrix)-(j+1)
            matrix[i][j] = result[sub][i]
