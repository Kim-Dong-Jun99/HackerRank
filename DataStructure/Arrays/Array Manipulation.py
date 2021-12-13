#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    storage = [0 for i in range(n)]
    for i in queries:
        storage[i[0] - 1] += i[2]
        if i[1] != n:
            storage[i[1]] -= i[2]
    maxVal = None
    tempVal = 0
    for i in storage:
        tempVal += i
        if maxVal == None:
            maxVal = tempVal
        elif maxVal < tempVal:
            maxVal = tempVal
    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
