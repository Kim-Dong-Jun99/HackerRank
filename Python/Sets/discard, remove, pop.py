n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    query = list(input().split())
    if query[0] == 'remove':
        if int(query[1]) in s:
            s.remove(int(query[1]))
    elif query[0] == 'discard':
        s.discard(int(query[1]))
    else:
        s.pop()

print(sum(s))