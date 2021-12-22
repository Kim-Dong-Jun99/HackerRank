#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def shortPalindrome(s):
    mod = 10 ** 9 + 7
    C1 = [0] * 26
    C2 = [0] * 26 * 26
    C3 = [0] * 26 * 26
    count = 0
    r26 = list(range(26))
    for c in s:
        k = ord(c) - 97
        p = 26 * k - 1
        q = k - 26
        for i in r26:
            q += 26
            p += 1
            count += C3[q]
            C3[p] += C2[p]
            C2[p] += C1[i]
        C1[k] += 1

    return count % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
