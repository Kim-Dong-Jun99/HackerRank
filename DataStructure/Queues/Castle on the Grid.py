#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    visited = [[startX, startY]]
    nextV = possibleWay(grid, startX, startY, visited)
    result = 1
    while ([goalX, goalY] in nextV) == False:
        temp = []
        visited += nextV[:]
        for i in nextV:

            for j in possibleWay(grid, i[0], i[1], visited):
                if (j in visited) == False:
                    temp.append(j)
        nextV = temp
        result += 1

    return result


def possibleWay(grid, i, j, visited):
    down = i - 1
    up = i + 1
    left = j - 1
    right = j + 1
    result = []
    while 0 <= down and ([down, j] in visited) == False:
        if grid[down][j] == 'X':
            break
        result.append([down, j])
        down -= 1
    while up < len(grid) and ([up, j] in visited) == False:
        if grid[up][j] == 'X':
            break
        result.append([up, j])
        up += 1
    while 0 <= left and ([i, left] in visited) == False:
        if grid[i][left] == 'X':
            break
        result.append([i, left])
        left -= 1
    while right < len(grid) and ([i, right] in visited) == False:
        if grid[i][right] == 'X':
            break
        result.append([i, right])
        right += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
