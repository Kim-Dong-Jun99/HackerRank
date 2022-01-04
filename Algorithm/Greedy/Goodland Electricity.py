#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    result = 0
    index = 0
    while index + k - 1 < len(arr) - 1:
        if index == 0 and result == 0:
            temp = index + k - 1
            if temp > len(arr) - 1:
                temp = len(arr) - 1
            while index < temp:
                if arr[temp] == 1:
                    break
                else:
                    temp -= 1
            if temp == index and arr[temp] == 0:
                return -1
            result += 1
            index = temp
        else:
            rightMost = index + 2 * k - 1
            if rightMost > len(arr) - 1:
                rightMost = len(arr) - 1
            while temp < rightMost:
                if arr[rightMost] == 1:
                    break
                else:
                    rightMost -= 1
            if index == rightMost:
                return -1
            index = rightMost
            result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
