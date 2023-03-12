import sys
input = sys.stdin.readline
N = int(input())

def tri(a):
    ex1 = [1]*a
    for i in range(3,a):
        ex1[i] = ex1[i-2] + ex1[i-3]
    print(ex1[-1])

for i in range(N):
    tri(int(input()))