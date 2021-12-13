#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    aNum = 0
    bNum = 0
    tempSum = 0
    i = 0
    while i < len(a):
        if tempSum + a[i] > maxSum:
            break
        else:
            tempSum += a[i]
            aNum += 1
            i += 1
    result = aNum
    j = 0
    while i > -1:
        while j < len(b):
            if tempSum + b[j] > maxSum:
                break
            else:
                tempSum += b[j]
                bNum += 1
                j += 1

        if aNum + bNum > result:
            result = aNum + bNum
        if i == 0:
            break
        tempSum -= a[i - 1]
        aNum -= 1
        i -= 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
