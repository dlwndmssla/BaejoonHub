#2589
import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []

for i in range(n):
    ex = list(map(str, input().rstrip()))
    graph.append(ex)
    
def bfs(graph, x,y, visited):
    visited[y][x] = 1
    queue = deque()
    queue.append([y,x])
    while queue:
        v = queue.popleft()
        y,x = v[0],v[1]
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0<=x0<=m-1 and 0<=y0<=n-1:
                if visited[y0][x0] == 0 and graph[y0][x0] == 'L':          
                    queue.append([y0,x0])
                    visited[y0][x0] = visited[y][x] + 1
vc0 = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'L':                
            visited = [[0 for i in range(m)] for j in range(n)]
            bfs(graph, x,y, visited)
            vc1 = max([max(visited[i]) for i in range(n)])
            vc0 = max(vc0,vc1)

print(vc0-1)
