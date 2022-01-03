#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    # Write your code here
    minus = min(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] - minus
    calc = [0 for i in range(max(arr) + 1)]

    for i in range(1, max(arr) + 1):
        if i == 1:
            calc[i] = 1
        elif i == 2:
            calc[i] = 1
        elif i == 5:
            calc[i] = 1
        else:
            calc[i] = getMin(calc, i) + 1
    result = 0
    for i in arr:
        result += calc[i]
    return result


def getMin(calc, i):
    temp = []
    if i - 1 >= 0:
        temp.append(calc[i - 1])
    if i - 2 >= 0:
        temp.append(calc[i - 2])
    if i - 5 >= 0:
        temp.append(calc[i - 5])
    return min(temp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
