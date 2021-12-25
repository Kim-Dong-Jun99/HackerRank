#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rankedSet = set(ranked)
    ranked = list(rankedSet)
    ranked.sort()
    result = list()
    rankIndex = 0
    inserted = False
    for i in range(len(player)):
        if rankIndex < len(ranked):
            for j in range(rankIndex, len(ranked)):
                inserted = False
                if ranked[j] > player[i]:
                    result.append(len(ranked) - j + 1)
                    rankIndex = j
                    inserted = True
                    break
                elif ranked[j] == player[i]:
                    result.append(len(ranked) - j)
                    rankIndex = j
                    inserted = True
                    break
            if inserted == False:
                result.append(1)
                for j in range(i + 1, len(player)):
                    result.append(1)
                return result
        else:
            result.append(1)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
