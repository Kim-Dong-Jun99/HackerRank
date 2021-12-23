#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    result = 0
    for i in range(1, len(s)):
        if i == 1:
            newS = list(set(s))
            for j in newS:
                if s.count(j) >= 2:
                    result += int(s.count(j) * (s.count(j) - 1) / 2)
        else:
            for j in range(len(s) - i):
                temp = s[j:j + i]
                tempSet = list(set(temp))
                for k in range(j + 1, len(s) - i + 1):
                    temp2 = s[k:k + i]
                    isAnagram = True
                    for l in tempSet:
                        if temp.count(l) != temp2.count(l):
                            isAnagram = False
                            break
                    if isAnagram:
                        result += 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
