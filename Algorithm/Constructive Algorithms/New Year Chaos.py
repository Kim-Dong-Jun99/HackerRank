#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    result = 0
    chaos = False
    i = len(q) - 1
    while i > 0:
        if q[i] != i + 1:
            j = i - 1
            while j > -1:
                if q[j] == i + 1:
                    break
                else:
                    j -= 1
            if i - j > 2:
                chaos = True
                break
            q = q[:j] + q[j + 1:i + 1] + q[j:j + 1] + q[i + 1:]
            result += i - j
        i -= 1

    if chaos:
        print('Too chaotic')
    else:
        print(result)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
