import sys
from math import prod
input = sys.stdin.readline

def bk(m,ans1,ans2):
    global cnt

    if m >= n:
        return

    ans1.append(num[m][0])
    ans2.append(num[m][1])

    a = abs(prod(ans1)-sum(ans2))
    
    # print(ans1,ans2,a)
    if cnt > a:
        cnt = a

    bk(m+1,ans1,ans2)
    
    ans1.pop()
    ans2.pop()
    bk(m+1,ans1,ans2)

n = int(input())
num = [list(map(int,input().split())) for i in range(n)]

cnt = 10e8
bk(0,[],[])

print(cnt)
