#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    if s1 == s2:
        return len(s1)
    else:
        LCS = [[0 for i in range(len(s1) + 1)] for j in range(len(s1) + 1)]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    LCS[i][j] = LCS[i - 1][j - 1] + 1
                else:
                    LCS[i][j] = max([LCS[i - 1][j], LCS[i][j - 1]])
        return LCS[len(s1)][len(s2)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
