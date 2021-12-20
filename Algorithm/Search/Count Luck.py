#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def countLuck(matrix, k):
    # Write your code here
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'M':
                visited = [[i, j]]
                route = [[i, j]]
                break

    result = 0
    while matrix[route[len(route) - 1][0]][route[len(route) - 1][1]] != '*':
        possible = possibleRoute(matrix, route[len(route) - 1][0], route[len(route) - 1][1])
        travel = True
        for i in possible:
            if (i in visited) == False:
                visited.append([i[0], i[1]])
                route.append([i[0], i[1]])
                travel = False
                break

        if travel:
            route.pop()

    result = checkChoice(matrix, route)
    if result == k:
        return 'Impressed'
    return 'Oops!'


def possibleRoute(matrix, i, j):
    result = []
    if 0 <= i - 1:
        if matrix[i - 1][j] == '.' or matrix[i - 1][j] == '*':
            result.append([i - 1, j])
    if i + 1 < len(matrix):
        if matrix[i + 1][j] == '.' or matrix[i + 1][j] == '*':
            result.append([i + 1, j])
    if 0 <= j - 1:
        if matrix[i][j - 1] == '.' or matrix[i][j - 1] == '*':
            result.append([i, j - 1])
    if j + 1 < len(matrix[0]):
        if matrix[i][j + 1] == '.' or matrix[i][j + 1] == '*':
            result.append([i, j + 1])
    return result


def checkChoice(matrix, route):
    result = 0
    for i in range(len(route) - 1):
        temp = possibleRoute(matrix, route[i][0], route[i][1])
        for j in temp:
            if (j in route) == False:
                result += 1
                break
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
