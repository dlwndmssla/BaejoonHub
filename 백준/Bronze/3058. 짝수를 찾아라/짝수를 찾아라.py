import sys, math
input = sys.stdin.readline
a = int(input())

for i in range(a):
    ex = list(map(int,input().split()))
    ex1 = []
    for j in range(7):
        if ex[j]%2 == 0:
            ex1.append(ex[j])
    print(*[sum(ex1), min(ex1)])