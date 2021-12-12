#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    count = [0 for i in range(201)]
    notice = 0
    for i in range(d):
        count[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        temp = 0
        for j in range(len(count)):
            temp += count[j]
            if temp >= math.ceil(d / 2):
                if d % 2 == 1:
                    if expenditure[i] >= 2 * j:
                        notice += 1
                    break
                else:
                    if temp == math.ceil(d / 2):
                        for k in range(j + 1, len(count)):
                            if count[k] != 0:
                                if expenditure[i] >= j + k:
                                    notice += 1
                                break
                    else:
                        if expenditure[i] >= 2 * j:
                            notice += 1
                    break
        count[expenditure[i]] += 1
        count[expenditure[i - d]] -= 1
    return notice


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
