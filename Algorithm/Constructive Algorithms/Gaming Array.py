#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    maxs = []
    curMax = None
    for i in range(len(arr)):
        if curMax == None:
            curMax = arr[i]
            maxs.append(i)
        elif arr[i] > curMax:
            curMax = arr[i]
            maxs.append(i)
    if len(maxs)%2 == 1:
        return 'BOB'
    else:
        return 'ANDY'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
