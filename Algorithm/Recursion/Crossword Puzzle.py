#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

def crosswordPuzzle(crossword, words):
    # Write your code here
    temp = words.split(';')
    if len(temp) == 1:
        # print('temp = %s'%temp)
        possible = canFit(crossword, temp[0])
        # print('possible = %s'%possible)
        return place(crossword, possible, temp[0])
    else:

        a = ';'.join(temp[1:])
        possibleCases = crosswordPuzzle(crossword, a)
        # print('temp = %s'%temp)
        # print('possibleCases = %s'%possibleCases)
        result = []
        for i in possibleCases:
            # print('i = %s'%i)
            possible = canFit(i, temp[0])
            if possible != []:
                for j in place(i, possible, temp[0]):
                    result.append(j)
        # print('result = %s'%result)
        return result


def canFit(crossword, word):
    temp = []
    for i in range(10):
        for j in range(10):
            if crossword[i][j] == '-' or crossword[i][j] == word[0]:
                horizontal = 1
                vertical = 1
                while j + horizontal < 10 and horizontal < len(word):
                    if crossword[i][j + horizontal] == '-' or crossword[i][j + horizontal] == word[horizontal]:
                        horizontal += 1
                    else:
                        break
                while i + vertical < 10 and vertical < len(word):
                    if crossword[i + vertical][j] == '-' or crossword[i + vertical][j] == word[vertical]:
                        vertical += 1
                    else:
                        break
                if horizontal == len(word):
                    if j == 0:
                        if j + horizontal == 10 or crossword[i][j + horizontal] != '-':
                            temp.append([i, j, 'h'])
                    elif crossword[i][j - 1] != '-':
                        if j + horizontal == 10 or crossword[i][j + horizontal] != '-':
                            temp.append([i, j, 'h'])
                if vertical == len(word):
                    if i == 0:
                        if i + vertical == 10 or crossword[i + vertical][j] != '-':
                            temp.append([i, j, 'v'])
                    elif crossword[i - 1][j] != '-':
                        if i + vertical == 10 or crossword[i + vertical][j] != '-':
                            temp.append([i, j, 'v'])
    return temp


def place(crossword, possible, word):
    result = []
    for i in possible:
        temp = []
        for j in crossword:
            temp.append(j[:])
        if i[2] == 'v':
            for j in range(len(word)):
                temp[i[0] + j] = temp[i[0] + j][:i[1]] + word[j] + temp[i[0] + j][i[1] + 1:]
        else:
            # for j in range(len(word)):
            #     crossword[i[0]] = crossword[i[0]][:i[1]+j]+word[j]+crossword[i[0]][i[1]+1+j:]
            temp[i[0]] = temp[i[0]][:i[1]] + word + temp[i[0]][i[1] + len(word):]
        result.append(temp)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result[0]))
    fptr.write('\n')

    fptr.close()
