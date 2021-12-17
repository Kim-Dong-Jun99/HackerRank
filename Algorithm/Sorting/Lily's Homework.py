#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    table = {}
    tableRev = {}
    for i in range(len(arr)):
        table[arr[i]] = i
        tableRev[arr[i]] = i
    arrCpy = arr[:]
    arrSorted = sorted(arr)
    arrReverse = sorted(arr)
    arrReverse.reverse()
    sortedSwap = 0
    reverseSwap = 0
    for i in range(len(arr)):
        if arr[i] != arrSorted[i]:
            sortedSwap += 1
            index = table[arrSorted[i]]
            table[arr[i]] = index
            arr[i], arr[index] = arrSorted[i], arr[i]
    for i in range(len(arr)):
        if arrCpy[i] != arrReverse[i]:
            reverseSwap += 1
            index = tableRev[arrReverse[i]]
            tableRev[arrCpy[i]] = index
            arrCpy[i], arrCpy[index] = arrReverse[i], arrCpy[i]
    return min(sortedSwap, reverseSwap)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)
    fptr.write(str(result) + '\n')

    fptr.close()
