#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        return grid
    elif n % 2 == 0:
        result = ''
        for i in range(len(grid[0])):
            result += 'O'
        return [result for j in range(len(grid))]
    else:
        temp = ''
        for i in range(len(grid[0])):
            temp += 'O'
        result = [temp for i in range(len(grid))]
        if n % 4 == 1:
            repeat = 2
        elif n % 4 == 3:
            repeat = 1
        for k in range(repeat):
            result = [temp for i in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 'O':
                        result[i] = result[i][:j] + '.' + result[i][j + 1:]
                        if i > 0:
                            result[i - 1] = result[i - 1][:j] + '.' + result[i - 1][j + 1:]
                        if i < len(grid) - 1:
                            result[i + 1] = result[i + 1][:j] + '.' + result[i + 1][j + 1:]
                        if j > 0:
                            result[i] = result[i][:j - 1] + '.' + result[i][j:]
                        if j < len(grid[0]) - 1:
                            result[i] = result[i][:j + 1] + '.' + result[i][j + 2:]
            grid = result
        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
