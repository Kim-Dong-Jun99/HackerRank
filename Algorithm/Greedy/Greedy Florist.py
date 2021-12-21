#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    sets = []
    temp = []
    for i in range(len(c) - 1, -1, -1):
        temp.append(c[i])
        if len(temp) == k or i == 0:
            sets.append(temp)
            temp = []

    result = 0
    temp1 = 1
    for i in sets:
        for j in i:
            result += temp1 * j
        temp1 += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
