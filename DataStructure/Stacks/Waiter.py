#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    primes = []
    compare = 2
    for i in range(q):
        if primes == []:
            primes.append(compare)
            compare += 1
        else:
            isPrime = False
            while isPrime == False:
                isPrime = True
                for j in primes:
                    if compare % j == 0:
                        isPrime = False
                        break
                if isPrime:
                    primes.append(compare)
                compare += 1
    answers = []
    A = number[:]
    B = []
    for i in primes:
        temp = []
        while A != []:
            tempsto = A.pop()
            if tempsto % i == 0:
                B.append(tempsto)
            else:
                temp.append(tempsto)
        while B != []:
            answers.append(B.pop())
        A = temp[:]
    while A != []:
        answers.append(A.pop())

    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
