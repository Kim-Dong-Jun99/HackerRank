#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    left = 0
    right = n - 1
    notNine = 0
    count = 0
    while left < right:
        if s[left] != s[right]:
            count += 1
        else:
            if s[left] != '9':
                notNine += 1
        left += 1
        right -= 1
    if k < count:
        return '-1'
    else:
        # temp = k - count
        left = 0
        right = n - 1
        while left < right:
            if s[left] != s[right]:
                if max(s[left], s[right]) != '9':
                    if k > count:
                        s = s[:left] + '9' + s[left + 1:right] + '9' + s[right + 1:]
                        k -= 2
                    else:
                        val = max(s[left], s[right])
                        s = s[:left] + val + s[left + 1:right] + val + s[right + 1:]
                        k -= 1
                else:
                    s = s[:left] + '9' + s[left + 1:right] + '9' + s[right + 1:]
                    k -= 1
                count -= 1
            else:
                if s[left] != '9':
                    if notNine > 0 and k > count and k >= 2:
                        notNine -= 1
                        s = s[:left] + '9' + s[left + 1:right] + '9' + s[right + 1:]
                        k -= 2
            left += 1
            right -= 1
        if n % 2 == 1 and k > 0:
            mid = int(n / 2)
            s = s[:mid] + '9' + s[mid + 1:]

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
