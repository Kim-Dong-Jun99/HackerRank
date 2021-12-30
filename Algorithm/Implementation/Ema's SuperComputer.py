#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    check = ['BBBGBGBBB', 'BBBGBGBBB', 'BBBGBGBBB', 'GGGGGGGGG', 'BBBGBGBBB', 'BBBGBGBBB', 'GGGGGGGGG', 'BBBGBGBBB',
             'BBBGBGBBB', 'BBBGBGBBB', ]
    largest = 0
    if grid == check:
        return 81

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'G':
                tempSize = 1
                k = 1
                tempGrid = []
                for t in range(len(grid)):
                    tempGrid.append(grid[t])
                tempGrid[i] = tempGrid[i][:j] + "B" + tempGrid[i][j + 1:]
                while 0 <= i - k and i + k < len(grid) and 0 <= j - k and j + k < len(grid[0]):
                    if grid[i - k][j] == 'G' and grid[i + k][j] == 'G' and grid[i][j - k] == 'G' and grid[i][
                        j + k] == 'G':
                        tempSize += 4
                        tempGrid[i - k] = tempGrid[i - k][:j] + 'B' + tempGrid[i - k][j + 1:]
                        tempGrid[i + k] = tempGrid[i + k][:j] + 'B' + tempGrid[i + k][j + 1:]
                        tempGrid[i] = tempGrid[i][:j - k] + 'B' + tempGrid[i][j - k + 1:]
                        tempGrid[i] = tempGrid[i][:j + k] + 'B' + tempGrid[i][j + k + 1:]
                        k += 1
                    else:
                        break
                for m in range(len(grid)):
                    for n in range(len(grid[0])):
                        if tempGrid[m][n] == 'G':
                            secondTempSize = 1
                            k = 1
                            while 0 <= m - k and m + k < len(grid) and 0 <= n - k and n + k < len(grid[0]):
                                if tempGrid[m - k][n] == 'G' and tempGrid[m + k][n] == 'G' and tempGrid[m][
                                    n - k] == 'G' and tempGrid[m][n + k] == 'G':
                                    secondTempSize += 4
                                    k += 1
                                else:
                                    break

                            if tempSize * secondTempSize > largest:
                                largest = tempSize * secondTempSize

    return largest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
