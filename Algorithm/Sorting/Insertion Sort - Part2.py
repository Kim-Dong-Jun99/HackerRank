#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        compare = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] > compare:
                arr[j + 1] = arr[j]
                if j == 0:
                    arr[j] = compare

            else:
                arr[j + 1] = compare
                break
        for j in arr:
            print(j, end=' ')
        print()


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
