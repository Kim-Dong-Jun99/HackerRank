#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    newTime = ''
    minSecond = s[2:8]
    if s[8:10] == 'AM':
        if s[0:2] == '12':
            newTime += '00'
        else:
            newTime += s[0:2]
    else:
        if s[0:2] == '12':
            newTime += '12'
        else:
            newTime += str(int(s[0:2]) + 12)

    newTime += minSecond

    return newTime


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
