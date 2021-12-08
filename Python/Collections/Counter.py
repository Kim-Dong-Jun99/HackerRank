# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
sizes = list(map(int, input().split()))
time = Counter(sizes)
m = int(input())
result = 0
for i in range(m):
    query = list(map(int, input().split()))
    if time[query[0]] > 0:
        result += query[1]
        time[query[0]] -= 1

print(result)