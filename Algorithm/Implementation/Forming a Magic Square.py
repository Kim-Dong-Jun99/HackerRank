#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    magicSquare = [[0 for x in range(3)] for y in range(3)]

    initList = [2, 4, 6, 8]

    minSum = None
    for i in initList:
        if i == 2 or i == 8:
            secondList = [4, 6]

        else:
            secondList = [2, 8]

        for j in secondList:
            magicSquare[0][0] = i
            magicSquare[0][2] = j

            magicSquare[1][1] = 5
            magicSquare[2][2] = 15 - 5 - i
            magicSquare[2][0] = 15 - 5 - j

            magicSquare[0][1] = 15 - i - j
            magicSquare[1][0] = 15 - i - magicSquare[2][0]
            magicSquare[1][2] = 15 - 5 - magicSquare[1][0]

            magicSquare[2][1] = 15 - magicSquare[2][2] - magicSquare[2][0]
            tempSum = 0

            for x in range(3):
                for y in range(3):
                    tempSum += abs(magicSquare[x][y] - s[x][y])

            if minSum == None:
                minSum = tempSum
            else:
                if minSum > tempSum:
                    minSum = tempSum

    return minSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
