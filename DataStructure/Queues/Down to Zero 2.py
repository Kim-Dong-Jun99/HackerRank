#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
results = [0 for i in range(10 ** 6 + 1)]


def downToZero(n):
    # Write your code here
    # results = [0 for i in range(n+1)]
    # if n >= 1:
    #     results[1] = 1
    # for i in range(2, n+1):
    #     if results[i] == 0:
    #         results[i] = results[i-1]+1
    #         j = 2
    #         while i*j <= n and j <= i:
    #             if results[i*j] == 0:
    #                 results[i*j] = results[i]+1
    #             else:
    #                 if results[i*j] > results[i]+1:
    #                     results[i*j] = results[i] + 1
    #             j += 1
    #     else:
    #         if results[i-1] + 1 < results[i]:
    #             results[i] = results[i-1]+1
    #         j = 2
    #         while i*j <= n and j <= i:
    #             if results[i*j] == 0:
    #                 results[i*j] = results[i]+1
    #             else:
    #                 if results[i*j] > results[i]+1:
    #                     results[i*j] = results[i] + 1
    #             j += 1
    return results[n]


def worstCase(n):
    results[1] = 1
    for i in range(2, n + 1):
        if results[i] == 0:
            results[i] = results[i - 1] + 1
            j = 2
            while i * j <= n and j <= i:
                if results[i * j] == 0:
                    results[i * j] = results[i] + 1
                else:
                    if results[i * j] > results[i] + 1:
                        results[i * j] = results[i] + 1
                j += 1
        else:
            if results[i - 1] + 1 < results[i]:
                results[i] = results[i - 1] + 1
            j = 2
            while i * j <= n and j <= i:
                if results[i * j] == 0:
                    results[i * j] = results[i] + 1
                else:
                    if results[i * j] > results[i] + 1:
                        results[i * j] = results[i] + 1
                j += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    worstCase(10 ** 6)

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
