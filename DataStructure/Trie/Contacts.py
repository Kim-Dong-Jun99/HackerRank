#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

class Node():
    def __init__(self, char):
        self.char = char
        self.child = {}
        self.childNum = 0


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        itr = self.head
        for i in string:
            if (i in itr.child) == False:
                itr.child[i] = Node(i)
            itr = itr.child[i]
            itr.childNum += 1

    def search(self, string):
        itr = self.head
        for i in string:
            if (i in itr.child) == False:
                return 0
            itr = itr.child[i]
        return itr.childNum


def contacts(queries):
    # Write your code here
    head = Trie()
    result = []
    for i in queries:

        if i[0] == 'add':
            head.insert(i[1])
        else:
            result.append(head.search(i[1]))
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
