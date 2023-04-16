import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
ex1 = []
for i in range(b):
    k = list(map(int, input().split()))
    ex1.append(k)
ex1.sort()
x = set()
x.add(1)
y = set()
for i in range(b):
    if 1 in set(ex1[i]):
        x.add(ex1[i][1])
    elif ex1[i][0] in x and ex1[i][1] not in x:
        y.add(ex1[i][1])
    elif ex1[i][1] in x and ex1[i][0] not in x:
        y.add(ex1[i][0])
print(len(x)+len(y)-1)