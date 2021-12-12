#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    compare = arr[n - 1]
    for i in range(n - 2, -1, -1):
        if arr[i] > compare:
            arr[i + 1] = arr[i]
            for j in range(n):
                print(arr[j], end=' ')
            print()
            if i == 0:
                arr[i] = compare
                for j in range(n):
                    print(arr[j], end=' ')
                print()
        else:
            arr[i + 1] = compare
            for j in range(n):
                print(arr[j], end=' ')
            print()
            break


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
