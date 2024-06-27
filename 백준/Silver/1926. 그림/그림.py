#그림
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,m = list(map(int,input().split()))

graph = [list(map(int,input().split())) for i in range(n)]


def bfs(v):
    global ans
    y,x = v
    visited[y][x] = True
    queue = deque([v])
    a1 = 1
    while queue:
        y,x = queue.popleft()
        for t in range(4):
            y0,x0 = y+[0,0,-1,1][t],x+[-1,1,0,0][t]
            if not ((0<= y0 <=n-1) and (0<= x0<=m-1)) : continue
            if visited[y0][x0]: continue
            if graph[y0][x0] == 0: continue
            visited[y0][x0] = True
            queue.append([y0,x0])
            a1 += 1
            
    ans.append(a1)
     
visited = [[False for i in range(m)] for j in range(n)]   
ans = [0]
for y1 in range(n):
    for x1 in range(m):
        if (graph[y1][x1] == 1) and not visited[y1][x1]:
            v = [y1,x1]
            bfs(v)

print(len(ans)-1)
print(max(ans))