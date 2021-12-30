#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    result = (len(A) * len(A[0])) * 2
    for i in range(len(A)):

        for j in range(len(A[0])):

            if j == 0:
                result += A[i][j]
                if len(A[0]) > 1:
                    result += abs(A[i][j] - A[i][j + 1])
            if j == len(A[0]) - 1:
                result += A[i][j]
            if 0 < j and j < len(A[0]) - 1:
                result += abs(A[i][j] - A[i][j + 1])

    for i in range(len(A[0])):

        for j in range(len(A)):

            if j == 0:
                result += A[j][i]
                if len(A) > 1:
                    result += abs(A[j][i] - A[j + 1][i])
            if j == len(A) - 1:
                result += A[j][i]
            if 0 < j and j < len(A) - 1:
                result += abs(A[j][i] - A[j + 1][i])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
