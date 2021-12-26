#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    left = c_q - 1
    right = n - c_q
    top = n - r_q
    bottom = r_q - 1
    # diagnal = (n-r_q+n-c_q)*2
    dRT = min([abs(n - r_q), abs(n - c_q)])
    dRB = min([abs(1 - r_q), abs(n - c_q)])
    dLT = min([abs(n - r_q), abs(1 - c_q)])
    dLB = min([abs(1 - r_q), abs(1 - c_q)])
    for i in range(k):
        if obstacles[i][0] == r_q:
            if obstacles[i][1] < c_q:
                if abs(c_q - obstacles[i][1] - 1) < left:
                    left = abs(c_q - obstacles[i][1] - 1)
            else:
                if abs(obstacles[i][1] - c_q - 1) < right:
                    right = abs(obstacles[i][1] - c_q - 1)
        elif obstacles[i][1] == c_q:
            if obstacles[i][0] < r_q:
                if abs(r_q - obstacles[i][0] - 1) < bottom:
                    bottom = abs(r_q - obstacles[i][0] - 1)
            else:
                if abs(obstacles[i][0] - r_q - 1) < top:
                    top = abs(obstacles[i][0] - r_q - 1)
        elif abs(obstacles[i][0] - r_q) == abs(obstacles[i][1] - c_q):
            if obstacles[i][0] > r_q and obstacles[i][1] > c_q:
                if abs(obstacles[i][0] - r_q - 1) < dRT:
                    dRT = abs(obstacles[i][0] - r_q - 1)
            elif obstacles[i][0] < r_q and obstacles[i][1] > c_q:
                if abs(r_q - obstacles[i][0] - 1) < dRB:
                    dRB = abs(r_q - obstacles[i][0] - 1)
            elif obstacles[i][0] > r_q and obstacles[i][1] < c_q:
                if abs(obstacles[i][0] - r_q - 1) < dLT:
                    dLT = abs(obstacles[i][0] - r_q - 1)
            elif obstacles[i][0] < r_q and obstacles[i][1] < c_q:
                if abs(r_q - obstacles[i][0] - 1) < dLB:
                    dLB = abs(r_q - obstacles[i][0] - 1)
    return right + left + top + bottom + dRT + dRB + dLT + dLB


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
