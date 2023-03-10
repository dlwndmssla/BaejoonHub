import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    ex1 = list(map(int, input().split()))
    b = (ex1[2])%ex1[0]
    if b == 0:
        b = ex1[0]
    c = int((ex1[2]-1)/ex1[0])+1
    print(100*b+c)