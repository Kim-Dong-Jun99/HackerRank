# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
query = list(map(list, input().split()))
query[0].sort()
for i in combinations_with_replacement(query[0], int(query[1][0])):
    for j in list(i):
        print(j, end = '')
    print()