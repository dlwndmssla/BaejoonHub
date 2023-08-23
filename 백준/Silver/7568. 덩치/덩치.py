import sys

n = int(input())
ex = []
for i in range(n):
    ex0 = list(map(int,input().split()))
    ex.append(ex0)

rank = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if (ex[i][0] < ex[j][0]) and (ex[i][1] < ex[j][1]):
            cnt +=1
    rank.append(cnt)
    
print(*rank)