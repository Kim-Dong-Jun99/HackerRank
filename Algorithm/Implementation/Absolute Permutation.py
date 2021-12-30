#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    result = []
    if k == 0:
        return list(range(1, n + 1))
    elif k > math.ceil(n / 2):
        return [-1]
    elif n % 2 == 0 and k == int(n / 2):
        return list(range(int(n / 2) + 1, n + 1)) + list(range(1, int(n / 2) + 1))
    else:
        for i in range(1, 1 + k):
            j = 1
            while i + j * k <= n:
                j += 1
            if j % 2 == 1:
                return [-1]
        for i in range(n):
            if i - k + 1 < 1:
                result.append(i + k + 1)
            elif i + k + 1 > n:
                result.append(i - k + 1)
            else:
                if result[i - k] == i + 1:
                    result.append(i - k + 1)
                else:
                    result.append(i + k + 1)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
