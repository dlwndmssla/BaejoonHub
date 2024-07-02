#미로탐색
import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m = list(map(int,input().split()))
 
graph = []
fire = []
for i in range(n):
    ex = list(map(str,input()))
    graph.append(ex)
    if 'J' in ex:
        jihun = [[i,ex.index('J')]]
    if 'F' in ex:
        for j in range(m):
            if ex[j] =='F': fire.append([i,j])
                

def bfs(fire,jihun):
    queue = deque(fire)
    while queue:
        y,x = queue.popleft()
        for t in range(4):
            y0,x0 = y+[0,0,-1,1][t],x+[-1,1,0,0][t]
            if not ((0<= y0 <=n-1) and (0<= x0<=m-1)) : continue
            if visited[y0][x0] != -1: continue
            if graph[y0][x0] in ['#','F']: continue
            graph[y0][x0] = 'F'
            visited[y0][x0] = visited[y][x]+1
            queue.append([y0,x0])

    queue = deque(jihun)
    while queue:
        y,x = queue.popleft()
        for t in range(4):
            y0,x0 = y+[0,0,-1,1][t],x+[-1,1,0,0][t]
            if not ((0<= y0 <=n-1) and (0<= x0<=m-1)) : continue
            if graph[y0][x0]  == '#': continue
            if visited[y0][x0] <= visited[y][x]+1 and visited[y0][x0] != -1: continue
            graph[y0][x0] = 'J'
            visited[y0][x0] = visited[y][x]+1
            queue.append([y0,x0])

visited = [[-1 for i in range(m) ]  for j in range(n) ]

for v in jihun:
    visited[v[0]][v[1]] = 0
for v in fire:
    visited[v[0]][v[1]] = 0
    
bfs(fire,jihun)

ans = []
for i in range(n):
    for j in range(m):
        if (i in [0,n-1] or j in [0, m-1] ) and graph[i][j] == 'J':
            ans.append(visited[i][j]+1)


if len(ans) != 0:
    print(min(ans))
else:
    print('IMPOSSIBLE')

