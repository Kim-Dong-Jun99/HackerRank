#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    # Write your code here
    tracks = {}
    for i in track:
        if (i[0] in tracks) == False:
            tracks[i[0]] = (i[1], i[2])
        else:
            temp = tracks[i[0]]
            # update = ()
            if i[1] > temp[0]:
                temp1 = temp[0]
            else:
                temp1 = i[1]
            if i[2] < temp[1]:
                temp2 = temp[1]
            else:
                temp2 = i[2]
            tracks[i[0]] = (temp1, temp2)

    result = n * m
    for i in tracks:
        temp = tracks[i]
        result -= temp[1] - temp[0] + 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
