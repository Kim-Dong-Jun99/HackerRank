#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    criteria = []
    for i in arr:
        criteria.append(i)
    criteria.sort()
    count = 0
    diffIndex = []
    for i in range(len(arr)):
        if arr[i] == criteria[i]:
            count += 1
        else:
            diffIndex.append(i)
    if count == len(arr):
        print('yes')
    elif len(diffIndex) == 2:
        print('yes')
        print('swap %d %d' % (diffIndex[0] + 1, diffIndex[1] + 1))
    else:
        canReverse = True
        occurence = 1
        for i in range(len(diffIndex) - 1):
            if diffIndex[i + 1] != diffIndex[i] + 1:
                if diffIndex[i + 1] == diffIndex[i] + 2:
                    if i == len(diffIndex) - 1 - i - 1 and len(diffIndex) % 2 == 0:
                        continue
                    else:
                        canReverse = False
                        break
                else:
                    canReverse = False
                    break
        if canReverse:
            success = True
            for i in range(len(diffIndex) - 1):
                if arr[diffIndex[i]] < arr[diffIndex[i + 1]]:
                    success = False
                    break
            if success:
                print('yes')
                print('reverse %d %d' % (diffIndex[0] + 1, diffIndex[len(diffIndex) - 1] + 1))
            else:
                print('no')
        else:
            print('no')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)



