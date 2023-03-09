import sys
input = sys.stdin.readline
N,M = map(int, input().split())
exam = [i+1 for i in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    c = exam[a-1:b][::-1]
    exam[a-1:b] = c
print(*exam)