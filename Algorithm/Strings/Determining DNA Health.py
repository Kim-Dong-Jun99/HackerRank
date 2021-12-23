#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())
    minV = None
    maxV = None
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]

        targetGenes = genes[first:last + 1]
        values = health[first:last + 1]
        searched = {}
        value = 0
        for i in range(len(targetGenes)):
            if (targetGenes[i] in searched):
                value += searched[targetGenes[i]] * values[i]
            else:
                appear = 0
                kmpTable = [-1, 0]
                for j in range(2, len(targetGenes[i]) + 1):
                    mid = int(j / 2)
                    while 0 < mid:
                        if targetGenes[i][:mid] == targetGenes[i][j - mid:j]:
                            break
                        else:
                            mid -= 1
                    kmpTable.append(mid)
                j = 0
                while j + len(targetGenes[i]) <= len(d):
                    temp = d[j:j + len(targetGenes[i])]
                    for k in range(len(temp) + 1):
                        if k == len(temp):
                            appear += 1
                            j += k - kmpTable[k]
                            break
                        elif targetGenes[i][k] != temp[k]:
                            j += k - kmpTable[k]
                            break

                searched[targetGenes[i]] = appear
                value += appear * values[i]
        if maxV == None:
            maxV = value
        elif maxV < value:
            maxV = value
        if minV == None:
            minV = value
        elif minV > value:
            minV = value
    print('%d %d' % (minV, maxV))
