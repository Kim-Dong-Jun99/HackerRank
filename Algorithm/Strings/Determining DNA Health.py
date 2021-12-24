#!/bin/python3

import math
import os
import random
import re
import sys


def buildBCT(pattern, bct):
    for i in range(len(pattern)):
        bct[ord(pattern[i]) - 97] = i


def buildGST(pattern, gst, suffix):
    patternSize = len(pattern)
    # suffix = [ 0 for i in range(patternSize+1)]
    # gst = [0 for i in range(patternSize+1)]

    # case 1
    i = patternSize
    j = i + 1
    suffix[i] = j
    while 0 < i:
        while j <= patternSize and pattern[i - 1] != pattern[j - 1]:
            if gst[j] == 0:
                gst[j] = j - i
            j = suffix[j]
        i -= 1
        j -= 1
        suffix[i] = j

    # case 2
    for i in range(patternSize + 1):
        if gst[i] == 0:
            gst[i] = j
        if i == j:
            j = suffix[j]


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
                patternSize = len(targetGenes[i])
                bct = [-1 for i in range(26)]
                suffix = [0 for i in range(patternSize + 1)]
                gst = [0 for i in range(patternSize + 1)]
                buildGST(targetGenes[i], gst, suffix)
                buildBCT(targetGenes[i], bct)

                j = 0
                while j + patternSize <= len(d):
                    k = patternSize - 1
                    while 0 <= k and targetGenes[i][k] == d[j + k]:
                        k -= 1
                    if k < 0:
                        appear += 1
                        j += max(gst[k + 1], k - bct[ord(d[j + k]) - 97])
                    else:
                        j += max(gst[k + 1], k - bct[ord(d[j + k]) - 97])

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
