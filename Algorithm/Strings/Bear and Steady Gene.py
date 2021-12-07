#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Write your code here
    genes = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    stan = int(len(gene) / 4)
    count = []
    for i in gene:
        if count == []:
            temp = [0, 0, 0, 0]
            temp[genes[i]] += 1
            count.append(temp)
        else:
            temp = count[len(count) - 1][:]
            temp[genes[i]] += 1
            count.append(temp)
    right = 0
    left = 0
    minLength = None
    while right < len(count):
        tempCount = 0
        for i in range(4):
            if count[len(count) - 1][i] - count[right][i] <= stan:
                tempCount += 1
        if tempCount == 4:
            while left < right:
                secondtemp = 0
                for i in range(4):
                    if count[len(count) - 1][i] - count[right][i] + count[left][i] <= stan:
                        secondtemp += 1
                if secondtemp == 4:
                    left += 1
                else:
                    break
            if minLength == None:
                minLength = right - left + 1
            elif minLength > right - left + 1:
                minLength = right - left + 1

        right += 1

    return minLength


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
