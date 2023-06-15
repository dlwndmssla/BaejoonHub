import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []

for i in range(n):
    ex = list(map(str, input().rstrip()))
    graph.append(ex)
     
def bfs(graph,x,y,visited):
    visited[y][x] = True
    queue = deque()
    node = [y,x]
    queue.append(node)
    count0[y][x] = 1
    while queue:
        v = queue.popleft()
        y, x = v[0], v[1]
        for t in range(4):
            x0 = x + [-1,1,0,0][t]
            y0 = y + [0,0,-1,1][t]
            if 0 <= x0 <= m-1 and 0 <= y0 <= n-1:
                if graph[y0][x0] == '1' and not visited[y0][x0]:
                    visited[y0][x0] = True
                    queue.append([y0,x0])
                    if count0[y0][x0] ==0:
                         count0[y0][x0] = count0[y][x]+1
                    
visited = [[False for i in range(m)] for j in range(n)]
count0 = [[0 for i in range(m)] for j in range(n)]
x,y = 0,0
bfs(graph,x,y,visited)
print(count0[-1][-1])              