#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    layers = int(min([len(matrix), len(matrix[0])]) / 2)

    row = len(matrix)
    column = len(matrix[0])

    for i in range(layers):
        tempSize = (row - 2) * 2 + (column - 2) * 2 + 4

        row -= 2
        column -= 2

        move = r % tempSize
        if move != 0:
            temp = []
            for k in range(i, len(matrix) - i):
                temp.append(matrix[k][i])
            temp.pop()
            for k in range(i, len(matrix[0]) - i):
                temp.append(matrix[len(matrix) - 1 - i][k])
            temp.pop()
            for k in range(len(matrix) - 1 - i, i - 1, -1):
                temp.append(matrix[k][len(matrix[0]) - 1 - i])
            temp.pop()
            for k in range(len(matrix[0]) - 1 - i, i - 1, -1):
                temp.append(matrix[i][k])
            temp.pop()

            temp = temp[len(temp) - move:] + temp[:len(temp) - move]
            tempIndex = 0
            for k in range(i, len(matrix) - i):
                matrix[k][i] = temp[tempIndex]
                tempIndex += 1
            for k in range(i + 1, len(matrix[0]) - i):
                matrix[len(matrix) - 1 - i][k] = temp[tempIndex]
                tempIndex += 1
            for k in range(len(matrix) - i - 2, i - 1, -1):
                matrix[k][len(matrix[0]) - 1 - i] = temp[tempIndex]
                tempIndex += 1
            for k in range(len(matrix[0]) - 2 - i, i, -1):
                matrix[i][k] = temp[tempIndex]
                tempIndex += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
