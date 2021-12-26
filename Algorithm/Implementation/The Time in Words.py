#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    hour = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    twentyMinutes = ['', '', 'twenty']
    tenMinutes = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eightteen',
                  'nineteen']
    minutes = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if m == 0:
        return hour[h] + " o' clock"
    elif 1 <= m and m <= 30:
        if m == 30:
            return 'half past ' + hour[h]
        elif m == 15:
            return 'quarter past ' + hour[h]
        else:
            if m // 10 == 2:
                return 'twenty ' + minutes[m % 10] + ' minutes past ' + hour[h]
            elif m // 10 == 1:
                return tenMinutes[m % 10] + ' minutes past ' + hour[h]
            elif m == 1:
                return 'one minute past ' + hour[h]
            else:
                return minutes[m % 10] + ' minutes past ' + hour[h]
    else:
        h += 1
        m = 60 - m

        if m == 15:
            return 'quarter to ' + hour[h]
        else:
            if m // 10 == 2:
                return 'twenty ' + minutes[m % 10] + ' minutes to ' + hour[h]
            elif m // 10 == 1:
                return tenMinutes[m % 10] + ' minutes to ' + hour[h]
            else:
                return minutes[m % 10] + ' minutes to ' + hour[h]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
