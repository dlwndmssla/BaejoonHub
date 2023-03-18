import sys
input = sys.stdin.readline
n = int(input())
ex1 = []
for i in range(n):
    ex2 = list(input().split())
    if ex2[0] == 'push':
        ex1.append(ex2[1])
    elif ex2[0] == 'pop':
        if len(ex1) != 0:
            print(ex1[-1])
            ex1 = ex1[:-1]
        else:
            print(-1)
    elif ex2[0] == 'size':
        print(len(ex1))
    elif ex2[0] == 'empty':
        if len(ex1) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(ex1) == 0:
            print(-1)
        else:
            print(ex1[-1])