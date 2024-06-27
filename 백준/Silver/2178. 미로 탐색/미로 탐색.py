#미로탐색
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,m = list(map(int,input().split()))

graph = [list(map(str,input())) for i in range(n)]

def bfs(v):
    y,x = v
    visited[y][x] = 1
    queue = deque([v])
    while queue:
        y,x = queue.popleft()
        cnt = visited[y][x]+1
        for t in range(4):
            y0,x0 = y+[0,0,-1,1][t],x+[-1,1,0,0][t]
            if not ((0<= y0 <=n-1) and (0<= x0<=m-1)) : continue
            if visited[y0][x0] != -1: continue
            if graph[y0][x0] == '0': continue
            visited[y0][x0] = cnt
            queue.append([y0,x0])

     
visited = [[-1 for i in range(m)] for j in range(n)]   

bfs([0,0])

print(visited[-1][-1])
