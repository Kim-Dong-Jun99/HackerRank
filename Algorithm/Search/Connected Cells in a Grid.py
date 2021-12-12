#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    maxArea = None
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[0]):
            if matrix[i][j] == 1:
                temp = []
                temp.append([i, j])
                nextCheck = check(matrix, i, j)
                while nextCheck != []:
                    pastTemp = temp[:]
                    for k in nextCheck:
                        if (k in temp) == False:
                            temp.append(k)
                    tempstor = nextCheck[:]
                    nextCheck = []
                    for k in tempstor:
                        if (k in pastTemp) == False:
                            nextCheck += check(matrix, k[0], k[1])
                if maxArea == None:
                    maxArea = len(temp)
                elif maxArea < len(temp):
                    maxArea = len(temp)
                for k in temp:
                    matrix[k[0]][k[1]] = 0
            else:
                j += 1
        i += 1

    return maxArea


def check(matrix, i, j):
    temp = []
    if i == 0:
        if j == len(matrix[0]) - 1:
            if matrix[i + 1][j - 1] == 1:
                temp.append([i + 1, j - 1])
            if matrix[i + 1][j] == 1:
                temp.append([i + 1, j])
            if matrix[i][j - 1] == 1:
                temp.append([i, j - 1])
        elif j == 0:
            if matrix[i][j + 1] == 1:
                temp.append([i, j + 1])
            if matrix[i + 1][j] == 1:
                temp.append([i + 1, j])
            if matrix[i + 1][j + 1] == 1:
                temp.append([i + 1, j + 1])
        elif 0 < j and j < len(matrix[0]) - 1:
            if matrix[i][j - 1] == 1:
                temp.append([i, j - 1])
            if matrix[i][j + 1] == 1:
                temp.append([i, j + 1])
            if matrix[i + 1][j - 1] == 1:
                temp.append([i + 1, j - 1])
            if matrix[i + 1][j] == 1:
                temp.append([i + 1, j])
            if matrix[i + 1][j + 1] == 1:
                temp.append([i + 1, j + 1])
    elif 0 < i and i < len(matrix) - 1:
        if j == len(matrix[0]) - 1:
            if matrix[i + 1][j - 1] == 1:
                temp.append([i + 1, j - 1])
            if matrix[i + 1][j] == 1:
                temp.append([i + 1, j])
            if matrix[i][j - 1] == 1:
                temp.append([i, j - 1])
            if matrix[i - 1][j - 1] == 1:
                temp.append([i - 1, j - 1])
            if matrix[i - 1][j] == 1:
                temp.append([i - 1, j])
        elif j == 0:
            if matrix[i][j + 1] == 1:
                temp.append([i, j + 1])
            if matrix[i + 1][j] == 1:
                temp.append([i + 1, j])
            if matrix[i + 1][j + 1] == 1:
                temp.append([i + 1, j + 1])
            if matrix[i - 1][j] == 1:
                temp.append([i - 1, j])
            if matrix[i - 1][j + 1] == 1:
                temp.append([i - 1, j + 1])
        elif 0 < j and j < len(matrix[0]) - 1:
            if matrix[i][j - 1] == 1:
                temp.append([i, j - 1])
            if matrix[i][j + 1] == 1:
                temp.append([i, j + 1])
            if matrix[i + 1][j - 1] == 1:
                temp.append([i + 1, j - 1])
            if matrix[i + 1][j] == 1:
                temp.append([i + 1, j])
            if matrix[i + 1][j + 1] == 1:
                temp.append([i + 1, j + 1])
            if matrix[i - 1][j] == 1:
                temp.append([i - 1, j])
            if matrix[i - 1][j + 1] == 1:
                temp.append([i - 1, j + 1])
            if matrix[i - 1][j - 1] == 1:
                temp.append([i - 1, j - 1])
    else:
        if 0 < j and j < len(matrix[0]) - 1:
            if matrix[i][j + 1] == 1:
                temp.append([i, j + 1])
            if matrix[i][j - 1] == 1:
                temp.append([i, j - 1])
        elif j == 0:
            if matrix[i][j + 1] == 1:
                temp.append([i, j + 1])
        else:
            if matrix[i][j - 1] == 1:
                temp.append([i, j - 1])
    return temp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
