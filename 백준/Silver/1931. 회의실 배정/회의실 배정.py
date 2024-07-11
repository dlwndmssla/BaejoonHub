import sys
input = sys.stdin.readline
n = int(input())
ex = []
max0 = 0
for i in range(n):
    ex1 = list(map(int, input().split()))
    max0 = max(max0,ex1[1])
    ex.append(ex1)

ex = sorted(ex, key=lambda x: (x[1], x[0]))
meetings = [ex[0]]
for i in range(1,n):
    if meetings[-1][1]<= ex[i][0]:
        meetings.append(ex[i])

print(len(meetings))