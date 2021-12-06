# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
rooms = list(map(int, input().split()))
set1 = set()
set2 = set()
for i in rooms:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)

set1.difference_update(set2)

print(set1.pop())