#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    # Write your code here
    limit = int(X ** (1 / N))
    possible = [i for i in range(1, limit + 1)]
    result = rc(X, N, possible, len(possible) - 1)
    return result


def rc(X, N, possible, index):
    if X == 0:
        return 1
    else:
        result = 0
        for i in range(index, -1, -1):
            if X - (possible[i] ** N) >= 0:
                result += rc(X - (possible[i] ** N), N, possible, i - 1)
        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
