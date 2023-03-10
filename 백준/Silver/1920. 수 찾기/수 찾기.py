import sys
input = sys.stdin.readline
N = int(input())
ex1 = set(map(int,input().split()))
M = int(input())
ex2 = list(map(int,input().split()))
for i in range(M):
    if ex2[i] in ex1:
        print(1)
    else:
        print(0)