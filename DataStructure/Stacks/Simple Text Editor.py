# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stack = []
string = ''
for i in range(n):
    query = list(input().split())
    if query[0] == '1':
        string += query[1]
        stack.append(['+',query[1]])
    elif query[0] == '2':
        stack.append(['-',string[len(string)-int(query[1]):]])
        string = string[:len(string) - int(query[1])]
    elif query[0] == '3':
        print(string[int(query[1])-1])
    elif query[0] == '4':
        temp = stack.pop()
        if temp[0] == '+':
            string = string[:len(string)-len(temp[1])]
        else:
            string += temp[1]
    # print(string)