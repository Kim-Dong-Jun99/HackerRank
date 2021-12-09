#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    storage = [[] for i in range(len(gb) * 2 + 1)]
    result = [None, None]
    for i in gb:
        storage[i[0]].append(i[1])
        storage[i[1]].append(i[0])
    # print(storage)
    for i in range(1, len(gb) + 1):
        if storage[i] != []:
            tempsto = set()
            tempsto.add(i)
            traverse = storage[i][:]
            nextTraverse = []
            while True:
                for j in traverse:
                    tempsto.add(j)
                    for k in storage[j]:
                        if (k in tempsto) == False:
                            nextTraverse.append(k)
                if nextTraverse == []:
                    break
                else:
                    traverse = nextTraverse[:]
                    nextTraverse = []
            if result[0] == None:
                result[0] = len(tempsto)
                result[1] = len(tempsto)
            else:
                if result[0] > len(tempsto):
                    result[0] = len(tempsto)
                if result[1] < len(tempsto):
                    result[1] = len(tempsto)
            # print(tempsto)
            for j in list(tempsto):
                storage[j] = []

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
