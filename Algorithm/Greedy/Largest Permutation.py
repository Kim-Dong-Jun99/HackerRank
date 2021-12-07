#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    # Write your code here
    if arr == list(range(len(arr), 0, -1)):
        return arr
    else:
        if k >= len(arr):
            arr.sort()
            arr.reverse()
            return arr
        else:
            i = 0
            index = 0
            value = {}
            for j in range(len(arr)):
                value[arr[j]] = j
            while i < k:
                tempIndex = value[len(arr) - index]
                if tempIndex != index:
                    temp = arr[index]

                    arr[index] = len(arr) - index
                    arr[tempIndex] = temp
                    value[temp] = tempIndex
                    index += 1
                    i += 1
                else:
                    index += 1
                if index == len(arr):
                    break
            return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
