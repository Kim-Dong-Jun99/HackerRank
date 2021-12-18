# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
mainstack = []
substack = []
# result = []
for i in range(n):
    query = list(map(int, input().rstrip().split()))
    # print(query)
    if query[0] == 1:
        mainstack.append(query[1])
    elif query[0] == 2:
        if substack == []:
            while mainstack != []:
                substack.append(mainstack.pop())
        substack.pop()
    else:
        if substack == []:
            while mainstack != []:
                substack.append(mainstack.pop())
        print(substack[len(substack) - 1])


